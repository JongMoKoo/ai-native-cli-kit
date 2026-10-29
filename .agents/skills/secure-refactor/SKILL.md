---
name: secure-refactor
description: Review input validation, unsafe eval/exec, shell commands, path traversal, secret handling, modularity, regression tests.
---
# secure-refactor

## When to use
Use for relevant local repository work only, subject to platform policies.

## Procedure
1. Read task, inspect files, list explicit acceptance criteria.
2. Identify data boundaries, edge cases, security and privacy constraints.
3. Implement smallest useful change; avoid speculative rewrites.
4. Add deterministic tests; execute tests and record evidence.
5. Summarize files changed, commands run, known limitations.

## Guardrails
No external transmission of task files; no fabricated test results; no updating exam-provided tools; no prohibited automation; no wholesale replacement of required work.
