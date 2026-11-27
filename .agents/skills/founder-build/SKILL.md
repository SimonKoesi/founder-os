---
name: founder-build
description: "Implement, debug, test or review software and automations in an existing project stack."
---
# founder-build

Use the user's project working directory. Inputs: project context, state, existing
artifacts and the requested outcome. Missing blocking evidence stays explicit.

Inspect code, callers, stack and tests before changes. For bugs use the bugfix workflow; for architecture, testing or review select the corresponding route. Preserve existing behavior and data. Use isolated side effects, confirm outcomes and verify retries. Do not prescribe a new stack by default.

Read [workflow](../../../workflows/implementation.md) and
[quality](../../../standards/quality.md) as relevant. Follow current authorization;
this skill grants no additional permissions or agent delegation.

Expected result: working changes, meaningful tests and state/handoff evidence. Save enduring decisions and actual checks in project
context/state/handoff; keep temporary diagnostics out of long-term context.
