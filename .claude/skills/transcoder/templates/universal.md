# Templates Universales (compatible con todos los agentes)

## Componente React/Vue

```
[ROLE] Expert {framework} developer

[TASK]
Create component {name}
- Props: {props}
- UI: {ui_description}
- Styling: {styling}

[CONTEXT]
File: {filepath}
Framework: {framework}

[OUTPUT]
- Code only, no explanations
- Include necessary imports
- {language} with TypeScript if applicable

[CONSTRAINTS]
- No verbose comments
- No example/demo code
- Follow {framework} best practices
```

## Endpoint API

```
[ROLE] Expert backend developer

[TASK]
Create API endpoint {method} {path}
1. Request validation: {request_schema}
2. Business logic: {logic}
3. Response format: {response_schema}

[CONTEXT]
File: {filepath}
Framework: {framework}
Database: {database}

[OUTPUT]
- Code only, no explanations
- Include error handling
- Max response: 800 tokens

[CONSTRAINTS]
- No verbose comments
- Follow REST conventions
- Security: validate inputs, sanitize outputs
```

## Función/Utilidad

```
[ROLE] Expert {language} developer

[TASK]
{description}
- Input parameters: {input_params}
- Output type: {output_type}
- Edge cases: {edge_cases}

[CONTEXT]
File: {filepath}
Language: {language}

[OUTPUT]
- Function code only
- No explanations
- Strict typing if language supports it

[CONSTRAINTS]
- No comments unless critical
- Pure function preferred
- Handle edge cases
```

## Database Schema/Migration

```
[ROLE] Database expert ({database})

[TASK]
Create schema/migration
- Tables: {tables}
- Relations: {relations}
- Indexes: {indexes}
- Constraints: {constraints}

[CONTEXT]
Database: {database}
ORM/Tool: {orm}

[OUTPUT]
- SQL or migration code only
- No explanations
- Include rollback if applicable

[CONSTRAINTS]
- No sample data
- No verbose comments
- Follow {database} conventions
```

## Test

```
[ROLE] Expert test engineer

[TASK]
Create tests for {target}
- Test cases: {test_cases}
- Coverage target: {coverage}%

[CONTEXT]
Source: {source_file}
Test file: {test_file}
Framework: {test_framework}

[OUTPUT]
- Test code only
- No explanations
- Use {test_framework} syntax

[CONSTRAINTS]
- No redundant tests
- Clear test names
- Arrange-Act-Assert pattern
```

## Refactor

```
[ROLE] Senior developer

[TASK]
Refactor {target}
- Goal: {goal}
- Preserve: {preserve}
- Improve: {improve}

[CONTEXT]
File: {filepath}
Current code:
{current_code}

[OUTPUT]
- Refactored code only
- No explanations
- Diff format preferred

[CONSTRAINTS]
- Minimal changes to achieve goal
- No breaking changes unless specified
- Maintain test compatibility
```

## Bug Fix

```
[ROLE] Debugging expert

[TASK]
Fix bug in {location}
- Error: {error_description}
- Expected: {expected}
- Actual: {actual}

[CONTEXT]
File: {filepath}
Relevant code: {code_snippet}

[OUTPUT]
- Fixed code only
- No explanations
- Minimal diff

[CONSTRAINTS]
- Fix root cause, not symptoms
- No unrelated refactors
- No breaking changes
- Test the fix mentally before responding
```

## Setup/Config

```
[ROLE] DevOps/Setup expert

[TASK]
{description}
Requirements:
{requirements}

[CONTEXT]
Project type: {project_type}
Stack: {stack}

[OUTPUT]
- Config files content
- Commands to execute (if needed)
- No explanations

[CONSTRAINTS]
- Production-ready configs
- No example/demo configs
- Security best practices
- Minimal dependencies
```

## Integration

```
[ROLE] Integration specialist

[TASK]
Integrate {service_a} with {service_b}
- Purpose: {purpose}
- Data flow: {data_flow}

[CONTEXT]
Files: {files}
Services: {services}
Auth: {auth_method}

[OUTPUT]
- Integration code only
- No explanations
- Include error handling

[CONSTRAINTS]
- Secure by default
- Handle failures gracefully
- No hardcoded credentials
```

## Performance Optimization

```
[ROLE] Performance engineer

[TASK]
Optimize {target}
- Current bottleneck: {bottleneck}
- Target improvement: {target}

[CONTEXT]
File: {filepath}
Current metrics: {metrics}
Stack: {stack}

[OUTPUT]
- Optimized code only
- No explanations
- Benchmark-ready

[CONSTRAINTS]
- Maintain correctness
- No premature optimization
- Profile before/after
```
