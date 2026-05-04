# Guías de Instalación de TransCoder

## 🎯 ¿Qué Nivel de Guía Necesitas?

TransCoder incluye **4 niveles** de guías de instalación para diferentes necesidades:

---

## 📚 Niveles de Documentación

### Nivel 0: Ultra-Rápido (30 segundos)

**Archivo:** Comandos directos
**Tiempo:** 30 segundos
**Para:** Usuarios experimentados

```bash
cd TransCoder
python install.py
python transcoder-cli.py
```

¡Listo!

---

### Nivel 1: Inicio Rápido (2 minutos) ⚡

**Archivo:** `QUICKSTART.md`
**Tamaño:** 2.5 KB
**Tiempo:** 2 minutos
**Para:** Primera vez con TransCoder

**Contenido:**
- ✅ Instalación (30 seg)
- ✅ Demo interactiva (1 min)
- ✅ Primer proyecto (30 seg)
- ✅ Uso del prompt
- ✅ Comandos básicos

**Cuándo usar:**
- Primera vez que instalas TransCoder
- Quieres probarlo rápidamente
- No quieres leer mucho

**Leer:**
```bash
cat QUICKSTART.md
```

---

### Nivel 2: Guía Completa Paso a Paso (15 minutos) 📖

**Archivo:** `INSTALL.md`
**Tamaño:** 11 KB
**Tiempo:** 15 minutos de lectura
**Para:** Instalación detallada con explicaciones

**Contenido:**

#### Tabla de Contenidos
1. Requisitos Previos
   - Sistema operativo
   - Python 3.8+
   - pip
   - Claude Code (opcional)

2. Instalación Automática
   - Descargar TransCoder
   - Ejecutar instalador
   - Verificación

3. Instalación Manual
   - Instalar dependencias
   - Configurar skill Claude Code
   - Configurar MCP server
   - Hacer CLI ejecutable

4. Configuración de Claude Code
   - Verificar skill instalada
   - Usar la skill
   - Configurar preferencias

5. Configuración de Otros Agentes
   - Cursor
   - Continue.dev
   - Windsurf / Otros

6. Verificación
   - Test 1: Python y dependencias
   - Test 2: MCP Server
   - Test 3: CLI
   - Test 4: Skill en Claude Code

7. Solución de Problemas
   - Error: "mcp module not found"
   - Error: "transcoder skill not found"
   - Error: MCP server no conecta
   - Error: "Python version too old"
   - CLI no muestra colores
   - Permisos denegados

8. Actualización
   - Actualizar desde Git
   - Actualizar desde ZIP

9. Desinstalación
   - Eliminar archivos
   - Eliminar configuraciones

10. Configuración Avanzada
    - Múltiples proyectos
    - Personalizar templates
    - Variables de entorno
    - Integración con IDEs

**Cuándo usar:**
- Primera instalación seria
- Tuviste problemas con instalación automática
- Quieres entender cada paso
- Necesitas configuración personalizada

**Leer:**
```bash
cat INSTALL.md
# O abre en tu editor favorito
```

---

### Nivel 3: Punto de Inicio Completo (5 minutos) 🚀

**Archivo:** `EMPEZAR-AQUI.md`
**Tamaño:** 3.9 KB
**Tiempo:** 5 minutos
**Para:** Orientación general y navegación

**Contenido:**
- ✅ Inicio ultra-rápido (3 pasos)
- ✅ Documentación por nivel (principiante → power user)
- ✅ Archivo a leer primero
- ✅ Solución de problemas
- ✅ Timeline sugerido
- ✅ Comandos más usados
- ✅ Checklist de primer uso

**Cuándo usar:**
- Acabas de descargar TransCoder
- No sabes por dónde empezar
- Quieres un roadmap de aprendizaje

**Leer:**
```bash
cat EMPEZAR-AQUI.md
```

---

## 🔧 Script de Instalación Automática

### `install.py` - Instalador Interactivo

**Archivo:** `install.py`
**Tamaño:** 9.6 KB (script Python)
**Tipo:** Instalador automático con interfaz colorida

**Funcionalidades:**

1. **Verificación de Python**
   - Chequea versión (requiere 3.8+)
   - Muestra versión actual

2. **Instalación de Dependencias**
   - Instala automáticamente desde `requirements.txt`
   - Muestra progreso

3. **Instalación de Skill Claude Code**
   - Detecta si tienes Claude Code
   - Copia skill automáticamente a `~/.claude/skills/`
   - Opción de sobrescribir si ya existe

4. **Configuración MCP Server**
   - Crea/actualiza `~/.claude/mcp.json`
   - Configura rutas absolutas
   - Merge con configuración existente

5. **Alias CLI**
   - Sugiere alias para terminal
   - Hace script ejecutable (Unix)

6. **Tests de Instalación**
   - Verifica MCP server
   - Verifica dependencias CLI
   - Verifica skill file

7. **Próximos Pasos**
   - Muestra cómo usar TransCoder
   - Comandos disponibles
   - Links a documentación

**Uso:**
```bash
python install.py
```

**Output esperado:**
```
============================================================
TransCoder - Instalador
============================================================

▶ Verificando Python...
✓ Python 3.10.5 ✓

▶ Instalando dependencias Python...
✓ Dependencias instaladas

▶ Instalando skill en Claude Code...
✓ Skill instalada en /home/usuario/.claude/skills/transcoder

▶ Configurando MCP server...
✓ MCP configurado en /home/usuario/.claude/mcp.json

▶ Configurando alias CLI...
Alias sugerido para tu shell:
  alias tc='python /path/to/TransCoder/transcoder-cli.py'

▶ Probando instalación...
✓ MCP server OK
✓ CLI dependencies OK
✓ Skill file OK

============================================================
¡Instalación completada!
============================================================

Próximos pasos:

1. Usar desde Claude Code:
   Simplemente di: "nuevo proyecto con transcoder"

2. Usar CLI directamente:
   python transcoder-cli.py

3. Comandos CLI disponibles:
   • tc new      - Nuevo proyecto
   • tc status   - Ver estado
   • tc next     - Siguiente paso
   • tc audit    - Auditar eficiencia

4. Documentación:
   Lee QUICKSTART.md y README.md para más detalles
```

---

## 📋 Comparación de Guías

| Guía | Tiempo | Nivel | Contenido | Cuándo Usar |
|------|--------|-------|-----------|-------------|
| **Comandos directos** | 30 seg | Expert | Mínimo | Ya sabes qué hacer |
| **QUICKSTART.md** | 2 min | Básico | Esencial | Primera vez, rápido |
| **INSTALL.md** | 15 min | Completo | Detallado | Instalación seria |
| **EMPEZAR-AQUI.md** | 5 min | Orientación | Roadmap | No sabes por dónde empezar |
| **install.py** | 1-2 min | Automático | Todo | Quieres instalación automática |

---

## 🎯 Recomendación por Perfil

### Nuevo Usuario (Primera Vez)
1. Lee **EMPEZAR-AQUI.md** (5 min)
2. Ejecuta **install.py** (1 min)
3. Lee **QUICKSTART.md** (2 min)
4. Empieza a usar

### Usuario con Experiencia
1. Ejecuta **install.py**
2. Empieza a usar

### Usuario que Tuvo Problemas
1. Lee **INSTALL.md** completo
2. Sección "Solución de Problemas"
3. Instalación manual si es necesario

### Power User
1. Revisa código de **install.py**
2. Instalación manual personalizada
3. Lee "Configuración Avanzada" en INSTALL.md

---

## 📁 Ubicación de Archivos

```
TransCoder/
├── EMPEZAR-AQUI.md          ← Punto de inicio
├── QUICKSTART.md            ← Guía rápida (2 min)
├── INSTALL.md               ← Guía completa (15 min)
├── install.py               ← Instalador automático
│
├── README.md                ← Documentación general
├── DEMO.md                  ← Tutoriales de uso
├── AGENTES-SOPORTADOS.md    ← Info sobre agentes
├── MODELOS-SOPORTADOS.md    ← Info sobre modelos
│
└── mcp-server/
    └── requirements.txt     ← Dependencias Python
```

---

## 🚀 Flujo de Instalación Recomendado

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. DESCARGAR TransCoder                                │
│     ├── Git: git clone ...                              │
│     └── ZIP: Descargar y extraer                        │
│                                                         │
│  2. LEER EMPEZAR-AQUI.md (5 min)                        │
│     └── Te orienta sobre qué leer                       │
│                                                         │
│  3. EJECUTAR install.py                                 │
│     └── Instalación automática                          │
│                                                         │
│  4. SI FALLA:                                           │
│     ├── Leer INSTALL.md sección "Problemas"            │
│     └── Instalación manual                              │
│                                                         │
│  5. VERIFICAR                                           │
│     ├── python transcoder-cli.py                        │
│     └── O en Claude Code: "transcoder status"           │
│                                                         │
│  6. PRIMER USO                                          │
│     └── Leer QUICKSTART.md                              │
│                                                         │
│  7. USO AVANZADO                                        │
│     └── Leer README.md y DEMO.md                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist de Instalación Exitosa

Marca cuando completes cada paso:

- [ ] Descargado TransCoder
- [ ] Leído EMPEZAR-AQUI.md
- [ ] Ejecutado `python install.py`
- [ ] Visto mensaje "¡Instalación completada!"
- [ ] Probado `python transcoder-cli.py`
- [ ] CLI muestra interfaz correctamente
- [ ] (Si usas Claude Code) Skill detectada
- [ ] Creado primer proyecto de prueba
- [ ] Generado primer prompt optimizado
- [ ] Leído QUICKSTART.md
- [ ] Leído README.md

---

## 🆘 Ayuda Rápida

### Problema: Instalación falló
**Solución:** Lee `INSTALL.md` sección "Solución de Problemas"

### Problema: No sé por dónde empezar
**Solución:** Lee `EMPEZAR-AQUI.md`

### Problema: Quiero probar rápido
**Solución:** Ejecuta `python install.py` y luego `python quickstart.py`

### Problema: Necesito entender cada paso
**Solución:** Lee `INSTALL.md` completo

---

## 📞 Soporte

Si después de leer las guías aún tienes problemas:

1. Revisa sección "Solución de Problemas" en INSTALL.md
2. Revisa logs de error completos
3. Verifica requisitos previos (Python 3.8+, pip)
4. Reporta issue en GitHub con:
   - Sistema operativo
   - Versión de Python
   - Error completo
   - Pasos que seguiste

---

<div align="center">

**4 Niveles de Guías para Todos los Usuarios**

[Inicio](EMPEZAR-AQUI.md) • [Rápido](QUICKSTART.md) • [Completo](INSTALL.md) • [Automático](install.py)

</div>
