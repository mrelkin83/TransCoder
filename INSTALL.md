# Guía de Instalación - TransCoder

Esta guía te llevará paso a paso para instalar y configurar TransCoder en tu sistema.

---

## Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Instalación Automática](#instalación-automática-recomendado)
3. [Instalación Manual](#instalación-manual)
4. [Configuración de Claude Code](#configuración-de-claude-code)
5. [Configuración de Otros Agentes](#configuración-de-otros-agentes)
6. [Verificación](#verificación)
7. [Solución de Problemas](#solución-de-problemas)

---

## Requisitos Previos

### Sistema Operativo
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu 20.04+, Debian, Fedora, etc.)

### Software Necesario

1. **Python 3.8 o superior**

   ```bash
   # Verificar versión
   python --version
   # o
   python3 --version
   ```

   Si no tienes Python instalado:
   - **Windows:** Descarga desde [python.org](https://www.python.org/downloads/)
   - **macOS:** `brew install python3`
   - **Linux:** `sudo apt install python3 python3-pip`

2. **pip (gestor de paquetes Python)**

   ```bash
   # Verificar pip
   pip --version
   # o
   pip3 --version
   ```

3. **Claude Code** (opcional pero recomendado)

   Si quieres usar TransCoder como skill en Claude Code, necesitas tenerlo instalado.
   - Descarga: [Claude Code](https://claude.com/claude-code)

---

## Instalación Automática (Recomendado)

La forma más rápida y sencilla:

### Paso 1: Descargar TransCoder

```bash
# Opción A: Si tienes git
git clone https://github.com/tu-usuario/transcoder.git
cd transcoder

# Opción B: Descargar ZIP
# Descarga el ZIP desde GitHub y descomprime
cd TransCoder
```

### Paso 2: Ejecutar Instalador

```bash
python install.py
```

El instalador hará automáticamente:
1. ✅ Verificar versión de Python
2. ✅ Instalar dependencias necesarias
3. ✅ Configurar skill en Claude Code (si está instalado)
4. ✅ Configurar MCP server
5. ✅ Probar la instalación
6. ✅ Mostrarte los siguientes pasos

### Paso 3: ¡Listo!

Si todo salió bien, verás:

```
============================================================
¡Instalación completada!
============================================================

Próximos pasos:

1. Usar desde Claude Code:
   Simplemente di: "nuevo proyecto con transcoder"

2. Usar CLI directamente:
   python transcoder-cli.py
```

---

## Instalación Manual

Si prefieres control total o el instalador automático falló:

### 1. Instalar Dependencias

```bash
cd TransCoder

# Instalar dependencias del MCP server
pip install -r mcp-server/requirements.txt

# Dependencias principales:
# - mcp>=0.9.0          (Model Context Protocol SDK)
# - click>=8.1.0        (CLI framework)
# - rich>=13.0.0        (Beautiful terminal output)
# - tiktoken>=0.5.0     (Token counting)
# - jinja2>=3.1.2       (Template rendering)
```

### 2. Instalar Skill en Claude Code

```bash
# Crear directorio de skills si no existe
mkdir -p ~/.claude/skills

# Copiar skill de TransCoder
cp -r .claude/skills/transcoder ~/.claude/skills/

# Verificar
ls ~/.claude/skills/transcoder
# Deberías ver: transcoder.md, config.json, templates/
```

### 3. Configurar MCP Server

Crear o editar `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "transcoder-mcp": {
      "command": "python",
      "args": [
        "/ruta/completa/a/TransCoder/mcp-server/server.py"
      ],
      "env": {
        "PYTHONPATH": "/ruta/completa/a/TransCoder",
        "TRANSCODER_ROOT": "/ruta/completa/a/TransCoder"
      }
    }
  }
}
```

**⚠️ IMPORTANTE:** Reemplaza `/ruta/completa/a/TransCoder` con la ruta real donde instalaste TransCoder.

Para obtener la ruta completa:

```bash
# En el directorio de TransCoder
pwd
# Linux/Mac: /home/usuario/TransCoder
# Windows: C:\Users\usuario\TransCoder
```

### 4. Hacer CLI Ejecutable (Opcional)

#### Linux/macOS:

```bash
# Hacer el script ejecutable
chmod +x transcoder-cli.py

# Crear alias permanente
echo "alias tc='python $(pwd)/transcoder-cli.py'" >> ~/.bashrc
# o si usas zsh:
echo "alias tc='python $(pwd)/transcoder-cli.py'" >> ~/.zshrc

# Recargar shell
source ~/.bashrc  # o source ~/.zshrc
```

#### Windows:

Crear un archivo `tc.bat` en una carpeta que esté en tu PATH:

```batch
@echo off
python C:\ruta\a\TransCoder\transcoder-cli.py %*
```

---

## Configuración de Claude Code

### Verificar que la Skill está Instalada

1. Abre Claude Code
2. En cualquier chat, escribe: `/skills`
3. Deberías ver `transcoder` en la lista

### Usar la Skill

Simplemente habla natural con Claude Code:

```
Tú: "Transcoder, nuevo proyecto: dashboard con React"

o

Tú: "Quiero crear un nuevo proyecto con transcoder"

o

Tú: "/tc nuevo proyecto"
```

Claude Code automáticamente:
1. Activará la skill TransCoder
2. Te pedirá detalles del proyecto
3. Generará un plan optimizado
4. Te guiará paso a paso

### Configurar Preferencias

Edita `~/.claude/skills/transcoder/config.json`:

```json
{
  "settings": {
    "auto_optimize_prompts": true,      // Optimizar prompts automáticamente
    "show_token_estimates": true,       // Mostrar estimaciones de tokens
    "compress_threshold": 400,          // Comprimir prompts >400 tokens
    "default_agent": "claude-code",     // Agente por defecto
    "language": "es"                    // Idioma (es/en)
  }
}
```

---

## Configuración de Otros Agentes

### Cursor

1. **Copiar Templates:**
   ```bash
   cp -r .claude/skills/transcoder/templates ~/.cursor/
   ```

2. **Usar desde Cursor:**
   ```
   Usa los comandos /composer generados por TransCoder CLI
   ```

### Continue.dev

Editar `~/.continue/config.json`:

```json
{
  "skills": [
    {
      "name": "transcoder",
      "path": "/ruta/a/TransCoder/.claude/skills/transcoder",
      "enabled": true
    }
  ]
}
```

### Windsurf / Otros

Usar **templates universales**:

1. Genera prompts con TransCoder CLI
2. Usa el formato "universal" que funciona con todos
3. Copia/pega en tu agente favorito

---

## Verificación

### Test 1: Python y Dependencias

```bash
# Verificar instalación de MCP
python -c "import mcp; print('MCP OK')"

# Verificar CLI dependencies
python -c "import click, rich; print('CLI OK')"
```

### Test 2: MCP Server

```bash
# Probar que el MCP server arranca
python mcp-server/server.py --help

# Si no hay errores, está OK
```

### Test 3: CLI

```bash
# Modo interactivo
python transcoder-cli.py

# Deberías ver el menú de TransCoder
```

### Test 4: Skill en Claude Code

1. Abre Claude Code
2. Escribe: "nuevo proyecto con transcoder"
3. Si Claude Code responde con formato TransCoder, ¡funciona!

---

## Solución de Problemas

### Error: "mcp module not found"

**Solución:**
```bash
pip install mcp --upgrade
```

### Error: "transcoder skill not found" en Claude Code

**Solución:**
```bash
# Verificar ubicación
ls ~/.claude/skills/transcoder

# Si no existe, copiar manualmente
cp -r .claude/skills/transcoder ~/.claude/skills/

# Reiniciar Claude Code
```

### Error: MCP server no conecta

**Solución:**

1. Verificar ruta en `~/.claude/mcp.json`
2. Asegurarse de usar rutas ABSOLUTAS (no relativas)
3. Verificar permisos:
   ```bash
   chmod +x mcp-server/server.py
   ```

### Error: "Python version too old"

**Solución:**
```bash
# Instalar Python 3.8+
# Ubuntu/Debian:
sudo apt install python3.10

# macOS:
brew install python@3.10

# Verificar
python3.10 --version
```

### CLI no muestra colores (Windows)

**Solución:**

Instalar dependencias adicionales:
```bash
pip install colorama
```

### Error: Permisos denegados (Linux/Mac)

**Solución:**
```bash
# Dar permisos de ejecución
chmod +x transcoder-cli.py
chmod +x mcp-server/server.py
chmod +x install.py
```

---

## Actualización

Para actualizar TransCoder a la última versión:

### Si instalaste con Git:

```bash
cd TransCoder
git pull origin main
pip install -r mcp-server/requirements.txt --upgrade
python install.py  # Re-ejecutar instalador
```

### Si descargaste ZIP:

1. Descarga la nueva versión
2. Reemplaza los archivos (mantén `.transcoder/` con tus proyectos)
3. Ejecuta `python install.py` nuevamente

---

## Desinstalación

Si necesitas desinstalar TransCoder:

```bash
# 1. Eliminar skill de Claude Code
rm -rf ~/.claude/skills/transcoder

# 2. Eliminar config MCP (editar ~/.claude/mcp.json)
# Elimina la sección "transcoder-mcp"

# 3. Eliminar archivos del proyecto
cd ..
rm -rf TransCoder

# 4. (Opcional) Desinstalar dependencias
pip uninstall mcp click rich tiktoken jinja2
```

---

## Configuración Avanzada

### Múltiples Proyectos

TransCoder crea un directorio `.transcoder/` en cada proyecto. Puedes trabajar en múltiples proyectos simultáneamente:

```bash
# Proyecto 1
cd ~/proyectos/mi-web
python ~/TransCoder/transcoder-cli.py new

# Proyecto 2
cd ~/proyectos/mi-api
python ~/TransCoder/transcoder-cli.py new
```

### Personalizar Templates

Edita los templates en `.claude/skills/transcoder/templates/`:

- `claude-code.md` - Templates para Claude Code
- `cursor.md` - Templates para Cursor
- `universal.md` - Templates universales

Formato de variables: `{variable_name}`

### Variables de Entorno

Puedes configurar variables de entorno:

```bash
# Configurar directorio raíz de TransCoder
export TRANSCODER_ROOT="/ruta/a/TransCoder"

# Configurar idioma por defecto
export TRANSCODER_LANG="es"

# Añadir a ~/.bashrc o ~/.zshrc para que sea permanente
```

---

## Integración con IDEs

### Visual Studio Code

1. Instalar extensión de Python
2. Abrir TransCoder como workspace
3. Usar terminal integrada para ejecutar CLI

### JetBrains (PyCharm, WebStorm, etc.)

1. Marcar `mcp-server/` como Sources Root
2. Configurar interpreter de Python
3. Usar terminal integrada

---

## Siguientes Pasos

Una vez instalado:

1. **Lee el README.md** para entender todas las funcionalidades
2. **Prueba crear tu primer proyecto:**
   ```bash
   python transcoder-cli.py new
   ```
3. **Experimenta con Claude Code:**
   ```
   "Nuevo proyecto con transcoder: [describe tu idea]"
   ```
4. **Audita tu eficiencia:**
   ```bash
   python transcoder-cli.py audit
   ```

---

## Soporte

¿Problemas con la instalación?

1. **Revisa esta guía** completa
2. **Verifica los requisitos** previos
3. **Prueba la instalación manual** si la automática falla
4. **Reporta issues** en GitHub con:
   - Sistema operativo
   - Versión de Python
   - Error exacto (mensaje completo)
   - Pasos que seguiste

---

<div align="center">

**¡Bienvenido a TransCoder!**

[Volver al README](README.md) • [Reportar Problema](https://github.com/tu-usuario/transcoder/issues)

</div>
