# Templates para OpenCode (GitHub Copilot)

## Componente React/Vue

```
@workspace Crear componente {name}

Context:
- File: {filepath}
- Framework: {framework}
- Props: {props}

Requirements:
{requirements}

Output:
- {language} code only
- No explanations
- Include imports

Constraints:
- No verbose comments
- No example code
- Follow {framework} conventions
```

## Endpoint API

```
@workspace Crear endpoint {method} {path}

Context:
- File: {filepath}
- Framework: {framework}
- Database: {database}

Request:
{request_schema}

Response:
{response_schema}

Validation:
{validation}

Output: Code only, include error handling
```

## Función/Utilidad

```
@workspace {description}

Context:
- File: {filepath}
- Language: {language}

Input: {input_params}
Output: {output_type}
Edge cases: {edge_cases}

Requirements:
- Pure function preferred
- Strict typing
- Handle edge cases

Output: Function code only, no explanations
```

## Database Schema/Migration

```
@workspace Create database schema

Context:
- Database: {database}
- ORM: {orm}

Tables:
{tables}

Relations:
{relations}

Indexes:
{indexes}

Output: SQL or migration code, include rollback
```

## Test

```
@workspace Create tests for {target}

Context:
- Source: {source_file}
- Test file: {test_file}
- Framework: {test_framework}

Test cases:
{test_cases}

Coverage target: {coverage}%

Output: Test code only, use {test_framework} syntax
```

## Refactor

```
@workspace Refactor {target}

Context:
- File: {filepath}
- Current code:
{current_code}

Goal: {goal}
Preserve: {preserve}
Improve: {improve}

Constraints:
- Minimal changes
- No breaking changes
- Maintain test compatibility

Output: Refactored code, diff format preferred
```

## Bug Fix

```
@workspace Fix bug in {location}

Context:
- File: {filepath}
- Error: {error_description}
- Expected: {expected}
- Actual: {actual}

Requirements:
- Fix root cause
- No unrelated changes
- Minimal diff

Output: Fixed code only
```

## Setup/Config

```
@workspace Setup {description}

Project: {project_type}
Stack: {stack}

Requirements:
{requirements}

Output:
- Config files
- Commands to run
- No verbose comments

Constraints:
- Production-ready
- Security best practices
- Minimal dependencies
```

## Integration

```
@workspace Integrate {service_a} with {service_b}

Context:
- Files: {files}
- Purpose: {purpose}
- Auth: {auth_method}

Data flow:
{data_flow}

Requirements:
- Secure by default
- Handle failures
- No hardcoded credentials

Output: Integration code only
```

## Performance Optimization

```
@workspace Optimize {target}

Context:
- File: {filepath}
- Bottleneck: {bottleneck}
- Current metrics: {metrics}

Target: {target_improvement}

Constraints:
- Maintain correctness
- No premature optimization
- Benchmark before/after

Output: Optimized code only
```

## CLI Command

```
@workspace Create CLI command {command_name}

Context:
- CLI framework: {cli_framework}
- Language: {language}

Functionality:
{functionality}

Arguments:
{arguments}

Options/Flags:
{options}

Output:
- Command implementation
- Help text
- Error handling

Constraints:
- Follow CLI framework conventions
- User-friendly error messages
```

## Docker/Container

```
@workspace Create Dockerfile for {project_type}

Stack: {stack}
Environment: {environment}

Requirements:
{requirements}

Output:
- Dockerfile
- .dockerignore
- docker-compose.yml (if needed)

Constraints:
- Multi-stage build if applicable
- Minimal image size
- Security best practices
```

## GitHub Actions Workflow

```
@workspace Create GitHub Actions workflow for {purpose}

Triggers: {triggers}

Steps:
{steps}

Environment: {environment}
Secrets needed: {secrets}

Output:
- .github/workflows/{name}.yml
- Complete workflow config

Constraints:
- Use official actions when possible
- Cache dependencies
- Fail fast on errors
```

---

## Formato Optimizado OpenCode

### Estructura General

```
@workspace {acción_específica}

Context:
{contexto_mínimo_necesario}

Requirements:
{requisitos_puntuales}

Output: {formato_esperado}
Constraints: {restricciones}
```

### Palabras Clave OpenCode

- `@workspace` - Para cambios en el workspace completo
- `@file` - Para cambios en archivo específico
- `@terminal` - Para comandos de terminal
- `#file:{path}` - Referencia explícita a archivo

### Ejemplo Optimizado

```
@workspace Create React component UserCard

Context:
#file:src/components/UserCard.tsx
Props: user: User (name, email, avatar)
Styling: Tailwind CSS

Requirements:
- Display user avatar (rounded)
- Show name and email
- Hover effect
- Mobile responsive

Output: TypeScript/JSX code only
Constraints: No PropTypes, use TypeScript interface
```

---

## Tips para OpenCode

1. **Usa @workspace para contexto amplio**
   ```
   @workspace Create authentication system
   ```

2. **Usa #file: para archivos específicos**
   ```
   #file:src/auth/login.ts
   ```

3. **Sé específico en Requirements**
   ```
   Requirements:
   - Use bcrypt for hashing
   - JWT tokens expire in 24h
   - Rate limit: 5 attempts/minute
   ```

4. **Especifica Output claramente**
   ```
   Output: TypeScript code only, no explanations
   ```

5. **Usa Constraints para evitar código innecesario**
   ```
   Constraints:
   - No comments unless critical
   - No example data
   - No unused imports
   ```
