# Templates para Gemini / Google AI Code

## Componente React/Vue

```
Task: Create {framework} component {name}

Context:
- File: {filepath}
- Framework: {framework} {version}
- Props interface: {props}
- Styling: {styling}

Requirements:
1. {requirement_1}
2. {requirement_2}
3. {requirement_3}

Output:
- {language} code only
- No explanations or markdown
- Include necessary imports

Constraints:
- No verbose comments
- No example/demo code
- Follow {framework} best practices
```

## Endpoint API

```
Task: Create API endpoint {method} {path}

Context:
- File: {filepath}
- Framework: {framework}
- Database: {database}

Request Schema:
{request_schema}

Response Schema:
{response_schema}

Validation Rules:
{validation}

Output:
- Code only, no explanations
- Include error handling
- Use async/await

Constraints:
- No verbose comments
- Security: sanitize inputs
- Follow REST conventions
```

## Función/Utilidad

```
Task: {description}

Context:
- File: {filepath}
- Language: {language}
- Purpose: {purpose}

Input Parameters:
{input_params}

Expected Output:
{output_type}

Edge Cases to Handle:
{edge_cases}

Output:
- Function code only
- Strict typing if supported
- No explanations

Constraints:
- Pure function preferred
- Handle all edge cases
- Optimal time complexity
```

## Database Schema

```
Task: Create database schema for {purpose}

Context:
- Database: {database}
- ORM/Tool: {orm}

Tables:
{tables_definition}

Relationships:
{relationships}

Indexes:
{indexes}

Constraints:
{constraints}

Output:
- SQL or migration code
- Include rollback
- No comments

Constraints:
- Normalized design
- Appropriate data types
- Foreign keys properly defined
```

## Test Suite

```
Task: Create comprehensive tests for {target}

Context:
- Source file: {source_file}
- Test file: {test_file}
- Framework: {test_framework}

Test Cases:
1. {test_case_1}
2. {test_case_2}
3. {test_case_3}

Coverage Target: {coverage}%

Output:
- Test code only
- Use {test_framework} syntax
- No explanations

Constraints:
- Follow AAA pattern (Arrange-Act-Assert)
- Clear test names
- Mock external dependencies
```

## Refactoring

```
Task: Refactor {target} to {goal}

Context:
- File: {filepath}
- Current implementation:
{current_code}

Refactoring Goals:
{goals}

Must Preserve:
{preserve}

Should Improve:
{improve}

Output:
- Refactored code only
- No explanations
- Clear diff if possible

Constraints:
- No breaking changes
- Maintain existing tests
- Improve readability/performance
```

## Bug Fix

```
Task: Fix bug in {location}

Bug Description:
{error_description}

Context:
- File: {filepath}
- Affected code:
{code_snippet}

Expected Behavior:
{expected}

Actual Behavior:
{actual}

Output:
- Fixed code only
- Minimal changes
- No refactoring beyond fix

Constraints:
- Address root cause
- No side effects
- Maintain backward compatibility
```

## Setup/Configuration

```
Task: Setup {project_type} project

Stack:
{stack}

Requirements:
1. {requirement_1}
2. {requirement_2}
3. {requirement_3}

Output:
- All configuration files
- Installation commands
- No verbose comments

Constraints:
- Production-ready
- Security best practices
- Minimal dependencies
- Latest stable versions
```

## Integration

```
Task: Integrate {service_a} with {service_b}

Context:
- Files: {files}
- Authentication: {auth_method}
- Data flow: {data_flow}

Integration Points:
{integration_points}

Error Handling:
{error_handling}

Output:
- Integration code only
- Include retry logic
- No explanations

Constraints:
- Secure credentials handling
- Graceful failure handling
- Logging for debugging
```

## Performance Optimization

```
Task: Optimize {target} for {metric}

Context:
- File: {filepath}
- Current metrics: {current_metrics}
- Bottleneck: {bottleneck}

Target Performance:
{target_metrics}

Profiling Data:
{profiling_data}

Output:
- Optimized code only
- No explanations
- Benchmark-ready

Constraints:
- Maintain correctness
- No premature optimization
- Measurable improvements
- Document complexity changes
```

## Data Processing Pipeline

```
Task: Create data pipeline for {purpose}

Context:
- Input format: {input_format}
- Output format: {output_format}
- Volume: {data_volume}

Pipeline Steps:
1. {step_1}
2. {step_2}
3. {step_3}

Error Handling:
{error_handling}

Output:
- Pipeline code only
- Include validation
- No explanations

Constraints:
- Handle large datasets efficiently
- Idempotent operations
- Proper error recovery
```

## AI/ML Model Integration

```
Task: Integrate {model_name} model

Context:
- Framework: {ml_framework}
- Model file: {model_path}
- Input/Output: {io_spec}

Preprocessing:
{preprocessing_steps}

Postprocessing:
{postprocessing_steps}

Output:
- Integration code only
- Include inference function
- No explanations

Constraints:
- Efficient inference
- Proper error handling
- Input validation
- Type safety
```

---

## Formato Optimizado Gemini

### Estructura Recomendada

```
Task: {acción_clara_y_específica}

Context:
{contexto_necesario}

Requirements/Steps:
{lista_numerada_de_requisitos}

Output:
- {formato_específico}
- No explanations

Constraints:
- {restricciones_clave}
```

### Palabras Clave Efectivas

- **Task:** Acción principal a realizar
- **Context:** Contexto mínimo necesario
- **Requirements:** Lista numerada de requisitos
- **Output:** Formato de salida esperado
- **Constraints:** Restricciones importantes

### Ejemplo Optimizado

```
Task: Create authentication middleware for Express.js

Context:
- File: src/middleware/auth.ts
- Framework: Express.js + TypeScript
- Auth method: JWT tokens

Requirements:
1. Verify JWT token from Authorization header
2. Decode user ID and role
3. Attach user info to request object
4. Return 401 if invalid/missing token
5. Return 403 if insufficient permissions

Output:
- TypeScript middleware function
- No explanations
- Include types

Constraints:
- Use jsonwebtoken library
- Handle expired tokens
- Validate token signature
- Type-safe request extension
```

---

## Tips para Gemini

1. **Sé muy específico en el Task**
   ```
   ❌ Task: Make it better
   ✅ Task: Optimize database query by adding index on user_id column
   ```

2. **Lista numerada en Requirements**
   ```
   Requirements:
   1. First requirement
   2. Second requirement
   3. Third requirement
   ```

3. **Especifica el Output claramente**
   ```
   Output:
   - Python code only
   - No markdown code blocks
   - No explanations
   ```

4. **Usa Constraints para calidad**
   ```
   Constraints:
   - Type hints required (Python)
   - No mutable default arguments
   - PEP 8 compliant
   ```

5. **Proporciona ejemplos si es necesario**
   ```
   Context:
   - Input example: {"name": "John", "age": 30}
   - Output example: User(name="John", age=30)
   ```
