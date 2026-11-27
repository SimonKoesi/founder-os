# Validation evidence

Environment: Windows PowerShell, Python 3.11.9, Codex CLI 0.171.0-alpha.13.2.
Final command outputs and source integrity confirmation are recorded in
`docs/validation-results.json` after the final validation run.

| Required simulation | Executed verification |
| --- | --- |
| New business idea | init idea, discovery route, context/state and resume status |
| New SaaS application | init saas, tenant isolation and billing/recovery profile |
| Small automation | init automation, duplicate-trigger/partial-failure/retry checks |
| Existing software project | adopt preserves source bytes and existing AGENTS/ignore content |
| New Codex session continuation | persisted handoff/state, pin verification, missing-binding recovery |
| Framework update | immutable install, matching bind, drift refusal, preview, apply, backup and rollback |
| Existing project bugfix | bugfix route resolves existing skill/workflow; upstream tool bugs reproduced and fixed with regressions |

These are executable contract/CLI simulations using isolated temporary data.
They are not claims of shipping a SaaS product, performing real business research
or proving autonomous model choices across new sessions. Test code is available
in `tests/test_framework.py`, `tests/test_regressions.py` and preserved tool tests.

Additional checks: broken local links outside code fences, route target existence,
skill frontmatter/naming, source mapping target coverage and archived source hashes,
runtime digest, high-confidence secret patterns, LF/CRLF portability, lock refusal,
rollback on injected failure, validation errors and nonfinite monetary input.
No external business URLs from ELEMENTE were followed.

The installed skill-creator `quick_validate.py` was attempted but cannot run because
PyYAML is absent. No dependency was installed. The framework's own validator checks
the deliberately simple supported frontmatter and paths for all 16 skills. This
does not replace an interactive Codex discovery smoke test, which remains unrun.

GitHub Actions is configured for Windows and Ubuntu, Python 3.11 and 3.13; remote CI
has not run. Live agents, production side effects and actual UI interaction have
not run. Secret scanning is heuristic; rights review is documented, not certified.
Project update performs compatible metadata rebinding only, not arbitrary major
schema migrations or rewriting project code. Unknown schemas fail without changes.
