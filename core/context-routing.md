# Context routing

1. Read project AGENTS and the four entry files named in its bridge. Verify the
   framework pin with `status`; resolve a mismatch before applying its standards.
2. Classify by intended outcome, project phase, type, size and risk. If a task
   crosses boundaries select multiple routes; e.g. a UI bug uses bugfix + design.
3. Read [routes](routes.json); the CLI `route TASK --project PATH` deterministically
   matches explicit route IDs or keywords and includes the current phase fallback.
   It is a suggestion, not semantic understanding. Review its reasons and adjust.
4. Read only returned workflows, standards and SKILL entrypoints. A skill may
   load its detailed method. The bridge can read central skills as files even
   when those skills are outside native discovery in the current project.
5. Identify current evidence, missing inputs, expected outputs and acceptance
   checks. Ask only for blocking choices; record provisional assumptions.
6. Execute, verify, and persist task outcomes using [state](project-state.md).

Global context: this router, selected reusable modules. Project context: project
identity, goals, boundaries, state, ADRs, evidence. Temporary context: debug output,
scratch calculations and task hypotheses; promote only verified enduring facts.
Do not save secrets or transcripts as project memory. Instruction loading is
explicit, not a promise that Markdown links are automatically followed by Codex.
Backlinks are navigation, not execution dependencies; workflow iteration is allowed.
