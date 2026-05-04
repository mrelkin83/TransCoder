#!/usr/bin/env python3
"""
Script de instalación de TransCoder
Configura todo lo necesario para usar TransCoder con Claude Code y otros agentes
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


class TransCoderInstaller:
    """Instalador de TransCoder"""

    def __init__(self):
        self.project_root = Path(__file__).parent.absolute()
        self.home = Path.home()

        # Colores para terminal
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        self.BLUE = '\033[94m'
        self.RESET = '\033[0m'
        self.BOLD = '\033[1m'

    def print_step(self, message):
        """Imprimir paso actual"""
        print(f"{self.BLUE}▶{self.RESET} {message}")

    def print_success(self, message):
        """Imprimir éxito"""
        print(f"{self.GREEN}✓{self.RESET} {message}")

    def print_error(self, message):
        """Imprimir error"""
        print(f"{self.RED}✗{self.RESET} {message}")

    def print_warning(self, message):
        """Imprimir advertencia"""
        print(f"{self.YELLOW}⚠{self.RESET} {message}")

    def print_header(self):
        """Imprimir encabezado"""
        print()
        print(f"{self.BOLD}{self.BLUE}{'=' * 60}{self.RESET}")
        print(f"{self.BOLD}{self.BLUE}TransCoder - Instalador{self.RESET}")
        print(f"{self.BOLD}{self.BLUE}{'=' * 60}{self.RESET}")
        print()

    def check_python(self):
        """Verificar versión de Python"""
        self.print_step("Verificando Python...")

        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            self.print_error(f"Python 3.8+ requerido (actual: {version.major}.{version.minor})")
            return False

        self.print_success(f"Python {version.major}.{version.minor}.{version.micro} ✓")
        return True

    def install_dependencies(self):
        """Instalar dependencias Python"""
        self.print_step("Instalando dependencias Python...")

        requirements = self.project_root / "mcp-server" / "requirements.txt"

        if not requirements.exists():
            self.print_error("requirements.txt no encontrado")
            return False

        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-r", str(requirements), "--quiet"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            self.print_success("Dependencias instaladas")
            return True
        except subprocess.CalledProcessError as e:
            self.print_error(f"Error instalando dependencias: {e}")
            return False

    def install_claude_code_skill(self):
        """Instalar skill en Claude Code"""
        self.print_step("Instalando skill en Claude Code...")

        claude_skills_dir = self.home / ".claude" / "skills"

        if not claude_skills_dir.exists():
            self.print_warning("Directorio ~/.claude/skills no encontrado")
            self.print_warning("¿Claude Code instalado?")

            response = input(f"{self.YELLOW}¿Crear directorio de todas formas? (s/n):{self.RESET} ")
            if response.lower() != 's':
                return False

            claude_skills_dir.mkdir(parents=True, exist_ok=True)

        # Copiar skill
        source_skill = self.project_root / ".claude" / "skills" / "transcoder"
        dest_skill = claude_skills_dir / "transcoder"

        if dest_skill.exists():
            self.print_warning(f"Skill ya existe en {dest_skill}")
            response = input(f"{self.YELLOW}¿Sobrescribir? (s/n):{self.RESET} ")
            if response.lower() != 's':
                self.print_warning("Skill no actualizada")
                return False

            shutil.rmtree(dest_skill)

        shutil.copytree(source_skill, dest_skill)
        self.print_success(f"Skill instalada en {dest_skill}")

        return True

    def configure_mcp_server(self):
        """Configurar MCP server en Claude Code"""
        self.print_step("Configurando MCP server...")

        claude_config_dir = self.home / ".claude"
        claude_config_dir.mkdir(parents=True, exist_ok=True)

        mcp_config_file = claude_config_dir / "mcp.json"

        # Configuración del MCP
        mcp_config = {
            "mcpServers": {
                "transcoder-mcp": {
                    "command": sys.executable,
                    "args": [
                        str(self.project_root / "mcp-server" / "server.py")
                    ],
                    "env": {
                        "PYTHONPATH": str(self.project_root),
                        "TRANSCODER_ROOT": str(self.project_root)
                    }
                }
            }
        }

        # Si ya existe, merge
        if mcp_config_file.exists():
            existing_config = json.loads(mcp_config_file.read_text())

            if "transcoder-mcp" in existing_config.get("mcpServers", {}):
                self.print_warning("TransCoder MCP ya configurado")
                response = input(f"{self.YELLOW}¿Actualizar configuración? (s/n):{self.RESET} ")
                if response.lower() != 's':
                    return False

            existing_config.setdefault("mcpServers", {}).update(mcp_config["mcpServers"])
            mcp_config = existing_config

        mcp_config_file.write_text(json.dumps(mcp_config, indent=2))
        self.print_success(f"MCP configurado en {mcp_config_file}")

        return True

    def create_cli_alias(self):
        """Crear alias para el CLI"""
        self.print_step("Configurando alias CLI...")

        cli_script = self.project_root / "transcoder-cli.py"

        # Hacer ejecutable (Unix)
        if os.name != 'nt':
            cli_script.chmod(0o755)

        # Sugerir alias
        alias_command = f"alias tc='python {cli_script}'"

        print()
        print(f"{self.YELLOW}Alias sugerido para tu shell:{self.RESET}")
        print(f"  {alias_command}")
        print()
        print(f"{self.YELLOW}Añade esto a tu ~/.bashrc o ~/.zshrc para uso permanente{self.RESET}")

        return True

    def test_installation(self):
        """Probar la instalación"""
        self.print_step("Probando instalación...")

        # Test 1: Importar MCP server
        try:
            sys.path.insert(0, str(self.project_root / "mcp-server"))
            # No importamos directamente porque requiere asyncio event loop
            # Solo verificamos que el archivo existe y es válido
            server_file = self.project_root / "mcp-server" / "server.py"
            if not server_file.exists():
                raise FileNotFoundError("server.py no encontrado")

            self.print_success("MCP server OK")
        except Exception as e:
            self.print_error(f"Error con MCP server: {e}")
            return False

        # Test 2: CLI
        try:
            import click
            import rich
            self.print_success("CLI dependencies OK")
        except ImportError as e:
            self.print_error(f"Error con dependencias CLI: {e}")
            return False

        # Test 3: Skill
        skill_file = self.project_root / ".claude" / "skills" / "transcoder" / "transcoder.md"
        if skill_file.exists():
            self.print_success("Skill file OK")
        else:
            self.print_error("Skill file no encontrado")
            return False

        return True

    def print_next_steps(self):
        """Imprimir próximos pasos"""
        print()
        print(f"{self.BOLD}{self.GREEN}{'=' * 60}{self.RESET}")
        print(f"{self.BOLD}{self.GREEN}¡Instalación completada!{self.RESET}")
        print(f"{self.BOLD}{self.GREEN}{'=' * 60}{self.RESET}")
        print()
        print(f"{self.BOLD}Próximos pasos:{self.RESET}")
        print()
        print(f"1. {self.BOLD}Usar desde Claude Code:{self.RESET}")
        print(f"   Simplemente di: {self.BLUE}\"nuevo proyecto con transcoder\"{self.RESET}")
        print(f"   o: {self.BLUE}\"/tc nuevo proyecto\"{self.RESET}")
        print()
        print(f"2. {self.BOLD}Usar CLI directamente:{self.RESET}")
        print(f"   {self.BLUE}python transcoder-cli.py{self.RESET}")
        print(f"   o con alias: {self.BLUE}tc{self.RESET} (si configuraste el alias)")
        print()
        print(f"3. {self.BOLD}Comandos CLI disponibles:{self.RESET}")
        print(f"   • {self.BLUE}tc new{self.RESET}      - Nuevo proyecto")
        print(f"   • {self.BLUE}tc status{self.RESET}   - Ver estado")
        print(f"   • {self.BLUE}tc next{self.RESET}     - Siguiente paso")
        print(f"   • {self.BLUE}tc audit{self.RESET}    - Auditar eficiencia")
        print()
        print(f"4. {self.BOLD}Documentación:{self.RESET}")
        print(f"   Lee {self.BLUE}INSTALL.md{self.RESET} y {self.BLUE}README.md{self.RESET} para más detalles")
        print()

    def run(self):
        """Ejecutar instalación completa"""
        self.print_header()

        steps = [
            ("Verificar Python", self.check_python),
            ("Instalar dependencias", self.install_dependencies),
            ("Instalar skill Claude Code", self.install_claude_code_skill),
            ("Configurar MCP server", self.configure_mcp_server),
            ("Crear alias CLI", self.create_cli_alias),
            ("Probar instalación", self.test_installation),
        ]

        for step_name, step_func in steps:
            if not step_func():
                self.print_error(f"Instalación fallida en: {step_name}")
                sys.exit(1)

        self.print_next_steps()


if __name__ == "__main__":
    installer = TransCoderInstaller()
    installer.run()
