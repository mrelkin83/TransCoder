# Templates para Cursor

## Componente React/Vue

```
/composer Crear componente {name}
--context {filepath}
--props {props}
--framework {framework}
--output-code-only
--typescript
```

## Endpoint API

```
/composer Crear endpoint {method} {path}
--context {filepath}
--framework {framework}
--request {request_schema}
--response {response_schema}
--validation {validation}
--output-code-only
```

## Función/Utilidad

```
/composer {description}
--context {filepath}
--input {input_params}
--output {output_type}
--language {language}
--typed
--output-code-only
```

## Database Schema

```
/composer Crear schema
--database {database}
--orm {orm}
--tables {tables}
--relations {relations}
--output-code-only
```

## Test

```
/composer Crear tests para {target}
--context {source_file} {test_file}
--framework {test_framework}
--cases {test_cases}
--output-code-only
```

## Refactor

```
/composer Refactorizar {target}
--context {filepath}
--goal {goal}
--preserve {preserve}
--improve {improve}
--output-code-only
```

## Bug Fix

```
/composer Fix bug: {error_description}
--context {filepath}
--expected {expected}
--actual {actual}
--minimal-changes
--output-code-only
```

## Setup/Config

```
/composer Setup {description}
--project {project_type}
--stack {stack}
--requirements {requirements}
--config-files-only
```
