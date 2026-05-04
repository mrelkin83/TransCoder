#!/usr/bin/env python3
"""
TransCoder CLI
Interfaz de línea de comandos para TransCoder

Uso:
    python transcoder-cli.py                    # Modo interactivo
    python transcoder-cli.py new                # Nuevo proyecto
    python transcoder-cli.py status             # Ver estado
    python transcoder-cli.py next               # Siguiente paso
"""

import json
import sys
import os
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime
import subprocess

try:
    import click
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    from rich.markdown import Markdown
    from rich import box
except ImportError:
    print("⚠️ Dependencias faltantes. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "click", "rich"])
    import click
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    from rich.markdown import Markdown
    from rich import box

# Consola Rich para output bonito
console = Console()


class TransCoderCLI:
    """Cliente CLI para TransCoder"""

    def __init__(self):
        self.project_root = Path.cwd()
        self.transcoder_dir = self.project_root / ".transcoder"
        self.project_file = self.transcoder_dir / "project.json"
        self.memory_file = self.transcoder_dir / "memory.json"

    def ensure_transcoder_dir(self):
        """Asegurar que existe el directorio .transcoder"""
        self.transcoder_dir.mkdir(exist_ok=True)

    def project_exists(self) -> bool:
        """Verificar si existe un proyecto activo"""
        return self.project_file.exists()

    def load_project(self) -> Optional[Dict]:
        """Cargar proyecto actual"""
        if not self.project_exists():
            return None
        return json.loads(self.project_file.read_text(encoding='utf-8'))

    def save_project(self, data: Dict):
        """Guardar proyecto"""
        self.ensure_transcoder_dir()
        data["last_updated"] = datetime.now().isoformat()
        self.project_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    def welcome(self):
        """Mensaje de bienvenida"""
        console.print()
        console.print(Panel.fit(
            "[bold cyan]TransCoder[/bold cyan] - Tu Traductor de Ideas a Código\n\n"
            "Optimiza prompts • Planifica proyectos • Ahorra tokens",
            border_style="cyan"
        ))
        console.print()

    def cmd_new_project(self):
        """Comando: Nuevo proyecto"""
        self.welcome()

        console.print("[bold yellow]📋 CONFIGURACIÓN INICIAL[/bold yellow]\n")

        # Preguntar datos
        name = Prompt.ask("[cyan]Nombre del proyecto[/cyan]")

        console.print("\n[cyan]Tipo de proyecto:[/cyan]")
        console.print("  1. Web (sitio web, landing, dashboard)")
        console.print("  2. App (móvil, desktop)")
        console.print("  3. API (backend, microservicio)")
        console.print("  4. CLI (herramienta línea de comandos)")
        console.print("  5. Script (automatización, utilidad)")
        type_choice = Prompt.ask("Elige", choices=["1", "2", "3", "4", "5"], default="1")

        type_map = {
            "1": "web",
            "2": "app",
            "3": "api",
            "4": "cli",
            "5": "script"
        }
        ptype = type_map[type_choice]

        stack_input = Prompt.ask("\n[cyan]Stack tecnológico[/cyan] (separado por comas)")
        stack = [s.strip() for s in stack_input.split(",")]

        feature = Prompt.ask("\n[cyan]Feature principal[/cyan] (máx 10 palabras)")

        # Crear proyecto
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
                "compress_prompts": True,
                "language": "es"
            },
            "token_savings": {
                "total_saved": 0,
                "percentage_vs_manual": 0
            },
            "decisions": []
        }

        self.save_project(project_data)

        console.print(f"\n[green]✅ Proyecto '{name}' creado correctamente[/green]")

        # Generar plan inicial
        if Confirm.ask("\n¿Generar plan inicial automáticamente?", default=True):
            self.generate_initial_plan(project_data)

    def generate_initial_plan(self, project: Dict):
        """Generar plan inicial basado en tipo de proyecto"""
        console.print("\n[yellow]🎯 Generando plan inicial...[/yellow]\n")

        # Plans predefinidos por tipo
        plans = {
            "web": [
                ("Setup", "Inicializar proyecto y dependencias"),
                ("Layout", "Estructura base y navegación"),
                ("Feature Core", f"Implementar {project['feature_principal']}"),
                ("Estilos", "UI/UX y responsive design"),
                ("Testing", "Tests y optimización")
            ],
            "api": [
                ("Setup", "Inicializar proyecto y configuración"),
                ("Database", "Modelos y migraciones"),
                ("Endpoints", f"Implementar {project['feature_principal']}"),
                ("Validación", "Seguridad y validación de inputs"),
                ("Testing", "Tests y documentación API")
            ],
            "app": [
                ("Setup", "Inicializar proyecto y estructura"),
                ("UI Base", "Pantallas principales y navegación"),
                ("Feature Core", f"Implementar {project['feature_principal']}"),
                ("Estado", "Gestión de estado y persistencia"),
                ("Testing", "Tests y optimización")
            ],
            "cli": [
                ("Setup", "Inicializar proyecto"),
                ("Commands", "Estructura de comandos"),
                ("Core Logic", f"Implementar {project['feature_principal']}"),
                ("Output", "Formateo y manejo de errores"),
                ("Testing", "Tests y documentación")
            ],
            "script": [
                ("Setup", "Estructura básica"),
                ("Core Logic", f"Implementar {project['feature_principal']}"),
                ("Testing", "Validación y tests")
            ]
        }

        steps = plans.get(project["type"], plans["script"])

        for i, (name, description) in enumerate(steps, 1):
            step = {
                "id": i,
                "name": name,
                "description": description,
                "status": "pending",
                "prompt_tokens": 0,
                "response_tokens": 0
            }
            project["steps"].append(step)

        self.save_project(project)

        # Mostrar plan
        table = Table(title="📋 Plan Generado", box=box.ROUNDED)
        table.add_column("#", style="cyan", width=4)
        table.add_column("Paso", style="yellow")
        table.add_column("Descripción", style="white")

        for step in project["steps"]:
            table.add_row(
                str(step["id"]),
                step["name"],
                step["description"]
            )

        console.print(table)
        console.print()

        if Confirm.ask("¿Empezar con el paso 1?", default=True):
            self.cmd_next_step()

    def cmd_status(self):
        """Comando: Ver estado del proyecto"""
        project = self.load_project()

        if not project:
            console.print("[red]❌ No hay proyecto activo[/red]")
            console.print("Usa: [cyan]python transcoder-cli.py new[/cyan]")
            return

        # Header
        console.print()
        console.print(Panel.fit(
            f"[bold]{project['project_name']}[/bold]\n"
            f"Tipo: {project['type']} • Stack: {', '.join(project['stack'])}",
            title="📊 Estado del Proyecto",
            border_style="cyan"
        ))
        console.print()

        # Progreso
        total_steps = len(project["steps"])
        completed = len(project["steps_completed"])
        percentage = int((completed / total_steps) * 100) if total_steps > 0 else 0

        console.print(f"[yellow]Progreso:[/yellow] {completed}/{total_steps} pasos ({percentage}%)")
        console.print(f"[yellow]Fase actual:[/yellow] {project['current_phase']}")

        # Tokens ahorrados
        savings = project.get("token_savings", {})
        if savings.get("total_saved", 0) > 0:
            console.print(f"[green]Ahorro de tokens:[/green] ~{savings['total_saved']} tokens")

        console.print()

        # Tabla de pasos
        if project["steps"]:
            table = Table(title="Pasos del Plan", box=box.ROUNDED)
            table.add_column("#", style="cyan", width=4)
            table.add_column("Estado", width=12)
            table.add_column("Paso", style="yellow")
            table.add_column("Descripción", style="white")

            for step in project["steps"]:
                status_icon = {
                    "completed": "[green]✅ Completado[/green]",
                    "in_progress": "[yellow]🔄 En curso[/yellow]",
                    "pending": "[dim]⏳ Pendiente[/dim]",
                    "skipped": "[dim]⏭️ Saltado[/dim]"
                }.get(step["status"], "❓")

                table.add_row(
                    str(step["id"]),
                    status_icon,
                    step["name"],
                    step["description"]
                )

            console.print(table)
            console.print()

        # Archivos en contexto
        if project.get("context_files"):
            console.print("[yellow]📁 Archivos en contexto:[/yellow]")
            for f in project["context_files"]:
                console.print(f"  • {f}")
            console.print()

    def cmd_next_step(self):
        """Comando: Ejecutar siguiente paso"""
        project = self.load_project()

        if not project:
            console.print("[red]❌ No hay proyecto activo[/red]")
            return

        # Encontrar siguiente paso pendiente
        next_step = None
        for step in project["steps"]:
            if step["status"] == "pending":
                next_step = step
                break

        if not next_step:
            console.print("[green]🎉 ¡Todos los pasos completados![/green]")
            return

        # Mostrar paso actual
        console.print()
        console.print(Panel.fit(
            f"[bold yellow]Paso {next_step['id']}/{len(project['steps'])}:[/bold yellow] {next_step['name']}\n\n"
            f"{next_step['description']}",
            title="🔄 Siguiente Paso",
            border_style="yellow"
        ))
        console.print()

        # Generar prompt optimizado
        prompt = self.generate_prompt_for_step(project, next_step)

        # Mostrar prompt
        console.print("[cyan]📝 PROMPT GENERADO:[/cyan]\n")
        console.print(Panel(
            prompt,
            border_style="cyan",
            box=box.ROUNDED
        ))
        console.print()

        # Estimar tokens
        tokens = len(prompt) // 4
        console.print(f"[dim]💰 Tokens estimados: ~{tokens}[/dim]")
        console.print(f"[dim]📊 Ahorro estimado vs manual: ~65%[/dim]\n")

        # Opciones
        console.print("[yellow]Opciones:[/yellow]")
        console.print("  1. Copiar al portapapeles")
        console.print("  2. Guardar en archivo")
        console.print("  3. Marcar como completado manualmente")
        console.print("  4. Saltar este paso")

        choice = Prompt.ask("¿Qué hacer?", choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            try:
                import pyperclip
                pyperclip.copy(prompt)
                console.print("[green]✅ Prompt copiado al portapapeles[/green]")
            except ImportError:
                console.print("[yellow]⚠️ pyperclip no instalado. Mostrando prompt arriba.[/yellow]")

        elif choice == "2":
            filename = f".transcoder/prompts/step-{next_step['id']}.md"
            Path(filename).parent.mkdir(parents=True, exist_ok=True)
            Path(filename).write_text(prompt, encoding='utf-8')
            console.print(f"[green]✅ Guardado en {filename}[/green]")

        elif choice == "3":
            self.complete_step(project, next_step['id'], tokens, tokens * 2)
            console.print("[green]✅ Paso marcado como completado[/green]")

        elif choice == "4":
            next_step["status"] = "skipped"
            self.save_project(project)
            console.print("[yellow]⏭️ Paso saltado[/yellow]")

        # Preguntar si continuar
        if choice in ["1", "2"] and Confirm.ask("\n¿Paso completado? (marca como hecho)", default=False):
            self.complete_step(project, next_step['id'], tokens, tokens * 2)

        if Confirm.ask("\n¿Continuar con siguiente paso?", default=False):
            self.cmd_next_step()

    def generate_prompt_for_step(self, project: Dict, step: Dict) -> str:
        """Generar prompt optimizado para un paso"""

        # Detectar tipo de tarea
        step_name_lower = step["name"].lower()

        # Templates base
        if "setup" in step_name_lower or "inicial" in step_name_lower:
            template = """🎯 TAREA: {task}

📦 PROYECTO:
- Nombre: {project_name}
- Tipo: {project_type}
- Stack: {stack}

✅ REQUERIMIENTOS:
{requirements}

📤 OUTPUT:
- Comandos a ejecutar (si aplica)
- Archivos a crear con contenido completo
- Configuraciones necesarias
- Sin explicaciones largas

🚫 NO INCLUIR:
- Comentarios verbose en código
- Archivos de ejemplo/demo innecesarios
"""
        else:
            template = """🎯 TAREA: {task}

📁 CONTEXTO:
- Proyecto: {project_name}
- Stack: {stack}
- Archivos clave: {context_files}

✅ REQUERIMIENTOS:
{requirements}

📤 OUTPUT:
- Código completo y funcional
- Sin explicaciones, solo código
- Seguir convenciones del stack

🚫 NO INCLUIR:
- Comentarios excesivos
- Código de ejemplo
- Archivos no solicitados
"""

        # Renderizar
        context_files = ", ".join(project.get("context_files", [])) or "ninguno aún"

        return template.format(
            task=step["description"],
            project_name=project["project_name"],
            project_type=project["type"],
            stack=", ".join(project["stack"]),
            requirements=f"• {step['description']}",
            context_files=context_files
        )

    def complete_step(self, project: Dict, step_id: int, prompt_tokens: int, response_tokens: int):
        """Marcar paso como completado"""
        for step in project["steps"]:
            if step["id"] == step_id:
                step["status"] = "completed"
                step["completed_at"] = datetime.now().isoformat()
                step["prompt_tokens"] = prompt_tokens
                step["response_tokens"] = response_tokens

                if step_id not in project["steps_completed"]:
                    project["steps_completed"].append(step_id)

                # Calcular ahorro
                total = prompt_tokens + response_tokens
                estimated_manual = int(total / 0.35)  # Asumiendo 65% ahorro
                saved = estimated_manual - total

                project["token_savings"]["total_saved"] += saved
                project["next_step_index"] = step_id + 1

                break

        self.save_project(project)

    def cmd_context_add(self, filepath: str):
        """Añadir archivo al contexto"""
        project = self.load_project()
        if not project:
            console.print("[red]❌ No hay proyecto activo[/red]")
            return

        if filepath not in project["context_files"]:
            project["context_files"].append(filepath)
            self.save_project(project)
            console.print(f"[green]✅ '{filepath}' añadido al contexto[/green]")
        else:
            console.print(f"[yellow]⚠️ '{filepath}' ya está en el contexto[/yellow]")

    def cmd_audit(self):
        """Auditar eficiencia de prompts"""
        project = self.load_project()
        if not project:
            console.print("[red]❌ No hay proyecto activo[/red]")
            return

        console.print()
        console.print(Panel.fit(
            "Análisis de Eficiencia de Prompts",
            title="🔍 Auditoría",
            border_style="cyan"
        ))
        console.print()

        # Calcular métricas
        completed_steps = [s for s in project["steps"] if s["status"] == "completed"]

        if not completed_steps:
            console.print("[yellow]No hay pasos completados para auditar[/yellow]")
            return

        total_prompt_tokens = sum(s.get("prompt_tokens", 0) for s in completed_steps)
        total_response_tokens = sum(s.get("response_tokens", 0) for s in completed_steps)
        total_tokens = total_prompt_tokens + total_response_tokens

        avg_prompt = total_prompt_tokens // len(completed_steps) if completed_steps else 0

        # Mostrar métricas
        table = Table(title="📊 Métricas Generales", box=box.ROUNDED)
        table.add_column("Métrica", style="cyan")
        table.add_column("Valor", style="yellow")

        table.add_row("Pasos completados", str(len(completed_steps)))
        table.add_row("Tokens prompts", f"{total_prompt_tokens:,}")
        table.add_row("Tokens respuestas", f"{total_response_tokens:,}")
        table.add_row("Total tokens", f"{total_tokens:,}")
        table.add_row("Promedio por prompt", f"{avg_prompt}")
        table.add_row("Ahorro estimado", f"~65%")

        console.print(table)
        console.print()

        # Recomendaciones
        console.print("[bold yellow]💡 Recomendaciones:[/bold yellow]\n")

        if avg_prompt > 500:
            console.print("  • [yellow]Prompts pesados[/yellow]: Considera activar compresión automática")

        if total_tokens > 10000:
            console.print("  • [green]Buen progreso[/green]: Has avanzado significativamente")

        if len(project.get("context_files", [])) > 10:
            console.print("  • [yellow]Mucho contexto[/yellow]: Revisa si todos los archivos son necesarios")

        console.print()

    def interactive_mode(self):
        """Modo interactivo"""
        self.welcome()

        # Verificar si hay proyecto activo
        if self.project_exists():
            project = self.load_project()
            console.print(f"[green]📂 Proyecto activo:[/green] {project['project_name']}\n")

            console.print("[yellow]¿Qué quieres hacer?[/yellow]")
            console.print("  1. Ver estado")
            console.print("  2. Siguiente paso")
            console.print("  3. Auditar eficiencia")
            console.print("  4. Nuevo proyecto")

            choice = Prompt.ask("Elige opción", choices=["1", "2", "3", "4"], default="2")

            if choice == "1":
                self.cmd_status()
            elif choice == "2":
                self.cmd_next_step()
            elif choice == "3":
                self.cmd_audit()
            elif choice == "4":
                if Confirm.ask("¿Estás seguro? Se creará un nuevo proyecto", default=False):
                    self.cmd_new_project()
        else:
            console.print("[yellow]No hay proyecto activo.[/yellow]\n")
            if Confirm.ask("¿Crear nuevo proyecto?", default=True):
                self.cmd_new_project()


# === CLI Commands ===

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """TransCoder CLI - Traductor de Ideas a Código Optimizado"""
    if ctx.invoked_subcommand is None:
        # Modo interactivo
        tc = TransCoderCLI()
        tc.interactive_mode()


@cli.command()
def new():
    """Crear nuevo proyecto"""
    tc = TransCoderCLI()
    tc.cmd_new_project()


@cli.command()
def status():
    """Ver estado del proyecto actual"""
    tc = TransCoderCLI()
    tc.cmd_status()


@cli.command()
def next():
    """Ejecutar siguiente paso"""
    tc = TransCoderCLI()
    tc.cmd_next_step()


@cli.command()
@click.argument('filepath')
def context(filepath):
    """Añadir archivo al contexto del proyecto"""
    tc = TransCoderCLI()
    tc.cmd_context_add(filepath)


@cli.command()
def audit():
    """Auditar eficiencia de prompts"""
    tc = TransCoderCLI()
    tc.cmd_audit()


if __name__ == "__main__":
    cli()
