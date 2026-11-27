# Persistent context contract

| File | Owns | Update trigger |
| --- | --- | --- |
| `.founder/project.json` | schema, name, type, size, stack, pinned framework version+digest | deliberate project/framework change |
| `.founder/context.md` | purpose, users, requirements, acceptance, boundaries, evidence links | approved scope or enduring evidence changes |
| `.founder/state.json` | phase, status, tasks, risks, last checks, next action | completed work or changed blocker |
| `.founder/decisions.md` | dated decisions and rationale; exceptions with expiry | meaningful tradeoff |
| `.founder/handoff.md` | current resume instruction and failed/pending checks | end of task/session |
| `.founder/roadmap.md` | outcomes, sequence and dependencies | planning changes |
| `.founder/local.json` | machine-specific central path | install/move; ignored by Git |

Project/state formats are JSON (also a YAML subset); no YAML dependency is needed.
State task entries: `id`, `title`, `status` in `todo/doing/done/blocked`.
Check entries: `command`, `result` in `passed/failed/not-run`, and `at` ISO date/time.
Unknown stack/requirements are explicit discovery tasks, not invented defaults.
Keep original documents, IDs and user input; link existing requirement sources.
Only one writer should update a project's state at a time; scripts use exclusive
creation/atomic replacement and refuse concurrent initialization/update.
Resume: read state/handoff, inspect actual tree and version control, verify claimed
checks when relevant, resolve drift, then do the next authorized task.
Completed tasks remain traceable; don't turn stale notes into current truth.
