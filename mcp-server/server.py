#!/usr/bin/env python3
"""
TransCoder MCP Server
Servidor de Model Context Protocol para TransCoder

Proporciona herramientas para:
- Gestión de sistema de archivos del proyecto
- Memoria persistente de decisiones y contexto
- Templates de prompts optimizados
- Cálculo de tokens
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
import asyncio

# MCP SDK (usaremos una implementación simplificada compatible)
try:
    from mcp.server import Server, NotificationOptions
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError:
    print("⚠️ MCP SDK no encontrado. Instalando...", file=sys.stderr)
    print("pip install mcp", file=sys.stderr)
    sys.exit(1)


class TransCoderMCPServer:
    """Servidor MCP para TransCoder"""

    def __init__(self):
        self.server = Server("transcoder-mcp")
        self.project_root = Path.cwd()
        self.transcoder_dir = self.project_root / ".transcoder"
        self.transcoder_dir.mkdir(exist_ok=True)

        # Archivos de estado
        self.project_file = self.transcoder_dir / "project.json"
        self.memory_file = self.transcoder_dir / "memory.json"
        self.context_file = self.transcoder_dir / "context.json"

        self._register_handlers()

    def _register_handlers(self):
        """Registrar todos los handlers de herramientas"""

        # === HERRAMIENTAS DE FILESYSTEM ===

        @self.server.list_tools()
        async def handle_list_tools() -> list[types.Tool]:
            """Lista todas las herramientas disponibles"""
            return [
                types.Tool(
                    name="tc_project_init",
                    description="Inicializar nuevo proyecto TransCoder",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "Nombre del proyecto"},
                            "type": {"type": "string", "enum": ["web", "app", "api", "cli", "desktop", "script"]},
                            "stack": {"type": "array", "items": {"type": "string"}, "description": "Stack tecnológico"},
                            "feature": {"type": "string", "description": "Feature principal (máx 10 palabras)"}
                        },
                        "required": ["name", "type", "stack", "feature"]
                    }
                ),
                types.Tool(
                    name="tc_project_read",
                    description="Leer estado actual del proyecto",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                types.Tool(
                    name="tc_project_update",
                    description="Actualizar estado del proyecto",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "updates": {"type": "object", "description": "Campos a actualizar"}
                        },
                        "required": ["updates"]
                    }
                ),
                types.Tool(
                    name="tc_step_add",
                    description="Añadir paso al plan de proyecto",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "Nombre del paso"},
                            "description": {"type": "string", "description": "Descripción detallada"}
                        },
                        "required": ["name", "description"]
                    }
                ),
                types.Tool(
                    name="tc_step_complete",
                    description="Marcar paso como completado",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "step_id": {"type": "integer", "description": "ID del paso a completar"},
                            "prompt_tokens": {"type": "integer", "description": "Tokens usados en el prompt"},
                            "response_tokens": {"type": "integer", "description": "Tokens de la respuesta"}
                        },
                        "required": ["step_id"]
                    }
                ),
                types.Tool(
                    name="tc_context_add",
                    description="Añadir archivo al contexto persistente",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "filepath": {"type": "string", "description": "Ruta del archivo"}
                        },
                        "required": ["filepath"]
                    }
                ),
                types.Tool(
                    name="tc_context_get",
                    description="Obtener contexto actual del proyecto",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                types.Tool(
                    name="tc_memory_set",
                    description="Guardar decisión o preferencia en memoria",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "key": {"type": "string", "description": "Clave de memoria (ej: 'auth_method')"},
                            "value": {"type": "object", "description": "Valor a guardar"}
                        },
                        "required": ["key", "value"]
                    }
                ),
                types.Tool(
                    name="tc_memory_get",
                    description="Recuperar valor de memoria",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "key": {"type": "string", "description": "Clave a recuperar"}
                        },
                        "required": ["key"]
                    }
                ),
                types.Tool(
                    name="tc_template_render",
                    description="Renderizar template de prompt optimizado",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "template_name": {"type": "string", "description": "Nombre del template"},
                            "agent": {"type": "string", "enum": ["claude-code", "cursor", "universal"], "description": "Agente objetivo"},
                            "variables": {"type": "object", "description": "Variables para renderizar"}
                        },
                        "required": ["template_name", "agent", "variables"]
                    }
                ),
                types.Tool(
                    name="tc_token_estimate",
                    description="Estimar tokens de un texto",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "text": {"type": "string", "description": "Texto a analizar"}
                        },
                        "required": ["text"]
                    }
                ),
                types.Tool(
                    name="tc_prompt_optimize",
                    description="Optimizar un prompt para reducir tokens",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string", "description": "Prompt original"},
                            "max_tokens": {"type": "integer", "description": "Máximo de tokens objetivo"}
                        },
                        "required": ["prompt"]
                    }
                )
            ]

        @self.server.call_tool()
        async def handle_call_tool(
            name: str, arguments: dict | None
        ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
            """Ejecutar herramienta solicitada"""

            args = arguments or {}

            # === PROYECTO ===

            if name == "tc_project_init":
                result = self._project_init(
                    args["name"],
                    args["type"],
                    args["stack"],
                    args["feature"]
                )
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            elif name == "tc_project_read":
                result = self._project_read()
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            elif name == "tc_project_update":
                result = self._project_update(args["updates"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            # === PASOS ===

            elif name == "tc_step_add":
                result = self._step_add(args["name"], args["description"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            elif name == "tc_step_complete":
                result = self._step_complete(
                    args["step_id"],
                    args.get("prompt_tokens", 0),
                    args.get("response_tokens", 0)
                )
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            # === CONTEXTO ===

            elif name == "tc_context_add":
                result = self._context_add(args["filepath"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            elif name == "tc_context_get":
                result = self._context_get()
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            # === MEMORIA ===

            elif name == "tc_memory_set":
                result = self._memory_set(args["key"], args["value"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            elif name == "tc_memory_get":
                result = self._memory_get(args["key"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            # === TEMPLATES ===

            elif name == "tc_template_render":
                result = self._template_render(
                    args["template_name"],
                    args["agent"],
                    args["variables"]
                )
                return [types.TextContent(type="text", text=result)]

            # === TOKENS ===

            elif name == "tc_token_estimate":
                result = self._token_estimate(args["text"])
                return [types.TextContent(type="text", text=json.dumps(result, indent=2))]

            elif name == "tc_prompt_optimize":
                result = self._prompt_optimize(
                    args["prompt"],
                    args.get("max_tokens", 400)
                )
                return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]

            else:
                raise ValueError(f"Herramienta desconocida: {name}")

    # === IMPLEMENTACIÓN DE HERRAMIENTAS ===

    def _project_init(self, name: str, ptype: str, stack: List[str], feature: str) -> Dict:
        """Inicializar proyecto"""
        project_data = {
            "project_name": name,
            "type": ptype,
            "stack": stack,
            "feature_principal": feature,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "current_phase": "planning",
            "steps": [],
            "steps_completed": [],
            "next_step_index": 0,
            "context_files": [],
            "preferences": {
                "auto_execute": False,
                "show_token_estimates": True,
                "compress_prompts": True
            },
            "token_savings": {
                "total_saved": 0,
                "percentage_vs_manual": 0
            },
            "decisions": []
        }

        self.project_file.write_text(json.dumps(project_data, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": f"Proyecto '{name}' inicializado correctamente",
            "project": project_data
        }

    def _project_read(self) -> Dict:
        """Leer proyecto actual"""
        if not self.project_file.exists():
            return {
                "success": False,
                "error": "No hay proyecto activo. Usa tc_project_init primero."
            }

        data = json.loads(self.project_file.read_text(encoding='utf-8'))
        return {
            "success": True,
            "project": data
        }

    def _project_update(self, updates: Dict) -> Dict:
        """Actualizar proyecto"""
        if not self.project_file.exists():
            return {"success": False, "error": "No hay proyecto activo"}

        data = json.loads(self.project_file.read_text(encoding='utf-8'))
        data.update(updates)
        data["last_updated"] = datetime.now().isoformat()

        self.project_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": "Proyecto actualizado",
            "project": data
        }

    def _step_add(self, name: str, description: str) -> Dict:
        """Añadir paso al plan"""
        if not self.project_file.exists():
            return {"success": False, "error": "No hay proyecto activo"}

        data = json.loads(self.project_file.read_text(encoding='utf-8'))

        step_id = len(data["steps"]) + 1
        step = {
            "id": step_id,
            "name": name,
            "description": description,
            "status": "pending",
            "prompt_tokens": 0,
            "response_tokens": 0
        }

        data["steps"].append(step)
        data["last_updated"] = datetime.now().isoformat()

        self.project_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": f"Paso '{name}' añadido",
            "step": step
        }

    def _step_complete(self, step_id: int, prompt_tokens: int, response_tokens: int) -> Dict:
        """Completar paso"""
        if not self.project_file.exists():
            return {"success": False, "error": "No hay proyecto activo"}

        data = json.loads(self.project_file.read_text(encoding='utf-8'))

        # Buscar paso
        step = next((s for s in data["steps"] if s["id"] == step_id), None)
        if not step:
            return {"success": False, "error": f"Paso {step_id} no encontrado"}

        # Actualizar paso
        step["status"] = "completed"
        step["completed_at"] = datetime.now().isoformat()
        step["prompt_tokens"] = prompt_tokens
        step["response_tokens"] = response_tokens

        # Actualizar lista completados
        if step_id not in data["steps_completed"]:
            data["steps_completed"].append(step_id)

        # Avanzar índice
        data["next_step_index"] = step_id + 1
        data["last_updated"] = datetime.now().isoformat()

        # Calcular ahorro de tokens (asumiendo 70% vs manual)
        total_tokens = prompt_tokens + response_tokens
        estimated_manual = int(total_tokens / 0.3)  # Si ahorramos 70%, el manual sería más
        saved = estimated_manual - total_tokens

        data["token_savings"]["total_saved"] += saved

        self.project_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": f"Paso {step_id} completado",
            "step": step,
            "tokens_saved": saved
        }

    def _context_add(self, filepath: str) -> Dict:
        """Añadir archivo al contexto"""
        if not self.project_file.exists():
            return {"success": False, "error": "No hay proyecto activo"}

        data = json.loads(self.project_file.read_text(encoding='utf-8'))

        if filepath not in data["context_files"]:
            data["context_files"].append(filepath)
            data["last_updated"] = datetime.now().isoformat()
            self.project_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": f"Archivo '{filepath}' añadido al contexto",
            "context_files": data["context_files"]
        }

    def _context_get(self) -> Dict:
        """Obtener contexto actual"""
        if not self.project_file.exists():
            return {"success": False, "error": "No hay proyecto activo"}

        data = json.loads(self.project_file.read_text(encoding='utf-8'))

        return {
            "success": True,
            "context_files": data["context_files"],
            "preferences": data["preferences"],
            "decisions": data.get("decisions", [])
        }

    def _memory_set(self, key: str, value: Any) -> Dict:
        """Guardar en memoria"""
        if self.memory_file.exists():
            memory = json.loads(self.memory_file.read_text(encoding='utf-8'))
        else:
            memory = {}

        memory[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }

        self.memory_file.write_text(json.dumps(memory, indent=2, ensure_ascii=False), encoding='utf-8')

        return {
            "success": True,
            "message": f"Memoria '{key}' guardada",
            "key": key,
            "value": value
        }

    def _memory_get(self, key: str) -> Dict:
        """Recuperar de memoria"""
        if not self.memory_file.exists():
            return {"success": False, "error": "No hay memoria guardada"}

        memory = json.loads(self.memory_file.read_text(encoding='utf-8'))

        if key not in memory:
            return {"success": False, "error": f"Clave '{key}' no encontrada"}

        return {
            "success": True,
            "key": key,
            "value": memory[key]["value"],
            "timestamp": memory[key]["timestamp"]
        }

    def _template_render(self, template_name: str, agent: str, variables: Dict) -> str:
        """Renderizar template"""
        templates_dir = Path(__file__).parent / "templates"

        # Mapeo de templates
        templates = {
            "component_react": {
                "claude-code": """🎯 TAREA: Crear componente React {name}

📁 CONTEXTO:
- Archivo: {filepath}
- Props: {props}

✅ REQUERIMIENTOS:
- Renderizar: {ui_description}
- Estilo: {styling}

📤 OUTPUT:
- Solo código TypeScript/JSX
- Sin explicaciones
- Imports necesarios al inicio

🚫 NO INCLUIR:
- Comentarios verbose
- Código de ejemplo
- PropTypes (usar TypeScript)""",
                "cursor": """/composer Crear componente React {name}
--context {filepath}
--props {props}
--output-code-only
--typescript""",
                "universal": """[ROLE] Expert React developer

[TASK]
Crear componente {name} que recibe props {props} y renderiza {ui_description}

[CONTEXT]
File: {filepath}
Styling: {styling}

[OUTPUT]
- TypeScript/JSX code only
- No explanations
- Include necessary imports"""
            },
            "endpoint_api": {
                "claude-code": """🎯 TAREA: Crear endpoint API {method} {path}

📁 CONTEXTO:
- Archivo: {filepath}
- Framework: {framework}

✅ REQUERIMIENTOS:
- Método: {method}
- Ruta: {path}
- Request body: {body_schema}
- Response: {response_schema}
- Validación: {validation}

📤 OUTPUT:
- Solo código
- Sin explicaciones
- Incluir manejo de errores básico

🚫 NO INCLUIR:
- Comentarios verbose
- Código de setup ya existente""",
                "universal": """[ROLE] Expert {framework} developer

[TASK]
Create API endpoint {method} {path}
- Request: {body_schema}
- Response: {response_schema}
- Validation: {validation}

[CONTEXT]
File: {filepath}

[OUTPUT]
- Code only, no explanations
- Include basic error handling
- Follow {framework} conventions"""
            }
        }

        if template_name not in templates:
            return f"❌ Template '{template_name}' no encontrado"

        template = templates[template_name].get(agent, templates[template_name]["universal"])

        # Renderizar con variables
        try:
            return template.format(**variables)
        except KeyError as e:
            return f"❌ Variable faltante: {e}"

    def _token_estimate(self, text: str) -> Dict:
        """Estimar tokens (aproximación: ~4 chars = 1 token)"""
        # Esta es una estimación simplificada
        # Para precisión real usar tiktoken
        chars = len(text)
        tokens = chars // 4

        return {
            "text_length": chars,
            "estimated_tokens": tokens,
            "note": "Estimación aproximada (4 chars ≈ 1 token)"
        }

    def _prompt_optimize(self, prompt: str, max_tokens: int = 400) -> Dict:
        """Optimizar prompt reduciendo tokens"""
        # Estimación actual
        current_tokens = len(prompt) // 4

        if current_tokens <= max_tokens:
            return {
                "optimized": False,
                "message": "El prompt ya está dentro del límite",
                "original_tokens": current_tokens,
                "target_tokens": max_tokens
            }

        # Optimizaciones simples
        optimized = prompt

        # Eliminar frases comunes innecesarias
        waste_phrases = [
            "por favor", "podrías", "me gustaría que",
            "sería bueno", "necesito que", "quiero que",
            "gracias", "thank you", "please"
        ]

        for phrase in waste_phrases:
            optimized = optimized.replace(phrase, "")

        # Eliminar espacios múltiples
        import re
        optimized = re.sub(r'\s+', ' ', optimized).strip()

        # Eliminar saltos de línea excesivos
        optimized = re.sub(r'\n\n+', '\n\n', optimized)

        new_tokens = len(optimized) // 4
        saved = current_tokens - new_tokens
        saved_pct = int((saved / current_tokens) * 100) if current_tokens > 0 else 0

        return {
            "optimized": True,
            "original_tokens": current_tokens,
            "new_tokens": new_tokens,
            "tokens_saved": saved,
            "percentage_saved": saved_pct,
            "optimized_prompt": optimized,
            "suggestions": [
                "Frases innecesarias eliminadas",
                "Espacios múltiples comprimidos",
                "Saltos de línea optimizados"
            ]
        }

    async def run(self):
        """Ejecutar servidor MCP"""
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="transcoder-mcp",
                    server_version="1.0.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    )
                )
            )


async def main():
    """Punto de entrada principal"""
    server = TransCoderMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
