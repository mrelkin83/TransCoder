# Templates para Claude Code

## Componente React/Vue

```
🎯 TAREA: Crear componente {name}

📁 CONTEXTO:
- Archivo: {filepath}
- Framework: {framework}
- Props: {props}

✅ REQUERIMIENTOS:
{requirements}

📤 OUTPUT:
- Solo código {language}
- Sin explicaciones
- Imports necesarios al inicio

🚫 NO INCLUIR:
- Comentarios verbose
- Código de ejemplo
- PropTypes (usar TypeScript si aplica)
```

## Endpoint API

```
🎯 TAREA: Crear endpoint {method} {path}

📁 CONTEXTO:
- Archivo: {filepath}
- Framework: {framework}

✅ REQUERIMIENTOS:
- Método HTTP: {method}
- Ruta: {path}
- Request body: {request_schema}
- Response: {response_schema}
- Validación: {validation}

📤 OUTPUT:
- Solo código
- Sin explicaciones
- Incluir manejo de errores básico

🚫 NO INCLUIR:
- Comentarios verbose
- Setup code ya existente
- Middleware duplicado
```

## Función/Utilidad

```
🎯 TAREA: {description}

📁 CONTEXTO:
- Archivo: {filepath}
- Lenguaje: {language}

✅ REQUERIMIENTOS:
- Input: {input_params}
- Output: {output_type}
- Casos especiales: {edge_cases}

📤 OUTPUT:
- Solo la función
- Sin explicaciones
- Tipado estricto si aplica

🚫 NO INCLUIR:
- Comentarios excesivos
- Código de test aquí
- Imports innecesarios
```

## Database Schema/Migration

```
🎯 TAREA: {description}

📁 CONTEXTO:
- Base de datos: {database}
- ORM/Tool: {orm}

✅ REQUERIMIENTOS:
- Tablas: {tables}
- Relaciones: {relations}
- Índices: {indexes}
- Constraints: {constraints}

📤 OUTPUT:
- SQL o código de migración
- Sin explicaciones
- Rollback incluido si aplica

🚫 NO INCLUIR:
- Datos de ejemplo
- Comentarios verbose
```

## Test

```
🎯 TAREA: Crear tests para {target}

📁 CONTEXTO:
- Archivo fuente: {source_file}
- Archivo test: {test_file}
- Framework: {test_framework}

✅ REQUERIMIENTOS:
- Casos a testear: {test_cases}
- Coverage mínimo: {coverage}

📤 OUTPUT:
- Solo código de test
- Sin explicaciones
- Usar {test_framework} syntax

🚫 NO INCLUIR:
- Comentarios excesivos
- Tests redundantes
- Setup code ya existente
```

## Refactor

```
🎯 TAREA: Refactorizar {target}

📁 CONTEXTO:
- Archivo: {filepath}
- Código actual: {current_code}

✅ REQUERIMIENTOS:
- Objetivo: {goal}
- Mantener: {preserve}
- Mejorar: {improve}

📤 OUTPUT:
- Código refactorizado completo
- Sin explicaciones
- Diff claro si aplica

🚫 NO INCLUIR:
- Comentarios explicativos largos
- Cambios no solicitados
- Breaking changes sin avisar
```

## Bug Fix

```
🎯 TAREA: Resolver bug en {location}

📁 CONTEXTO:
- Archivo: {filepath}
- Error: {error_description}
- Comportamiento esperado: {expected}
- Comportamiento actual: {actual}

✅ REQUERIMIENTOS:
- Fix mínimo necesario
- No romper funcionalidad existente
- Sin refactor innecesario

📤 OUTPUT:
- Solo el código modificado
- Sin explicaciones largas
- Diff claro

🚫 NO INCLUIR:
- Refactors no relacionados
- Comentarios excesivos
- Cambios estéticos
```

## Setup/Config

```
🎯 TAREA: {description}

📁 CONTEXTO:
- Proyecto: {project_type}
- Stack: {stack}

✅ REQUERIMIENTOS:
{requirements}

📤 OUTPUT:
- Archivos de configuración completos
- Comandos a ejecutar (si aplica)
- Sin explicaciones largas

🚫 NO INCLUIR:
- Configuraciones de ejemplo
- Comentarios verbose en configs
- Dependencias innecesarias
```
