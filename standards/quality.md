# Quality contract

Before implementation: define observable success, caller compatibility and the
affected failure/cancel/retry/back-navigation paths. Retain IDs, data and inputs.
Success requires a confirmed operation result; retries must not duplicate effects.
Use isolated data for external side effects and keep secrets out of logs/fixtures.

Verify in proportion to risk: run existing affected tests; add regression tests
for nontrivial failure modes, parsers, persistence, money and permissions. Report
commands, results and limits. A static check does not prove model behavior or UI.
Inspect diff for unrelated changes, unsupported claims and sensitive content.
Record outstanding risk with owner/next step. Failures preserve user input and
offer a retry; cancellation leaves recoverable state.

Framework acceptance: `python scripts/founder.py validate`, then unittest discovery.
The validator checks local Markdown links outside fenced code, routes, skills,
schema contracts, migration target coverage and high-confidence secret patterns.
It does not prove legal ownership, detect every secret, execute remote CI or
certify production security. Use human review before external publication.
