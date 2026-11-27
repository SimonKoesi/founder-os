# Codex compatibility — checked 2026-11-27

Locally observed: codex-cli 0.171.0-alpha.13.2; Python 3.11.9; Git 2.54.0.windows.1;
GitHub CLI 2.101.0. The CLI version command succeeded with temporary alias cleanup
warnings. No second interactive Codex instance or autonomous agent swarm was run.

The current official manual was fetched using the installed openai-docs helper.
Relevant official guides:

- [Skill structure and discovery](https://learn.chatgpt.com/docs/build-skills):
  SKILL.md with name/description, progressive loading, repository `.agents/skills`,
  user skill locations and symlink support.
- [AGENTS discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md):
  global then repository-to-working-directory guidance, one file per directory,
  override precedence and default combined byte cap.
- [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference):
  configuration is distinct from instructions; this framework does not change
  global sandbox, model, MCP or approval defaults.

Implementation uses repository-local `.agents/skills/<name>/SKILL.md` with plain
name/description frontmatter. Skills use supported metadata only; optional UI
metadata is omitted. User invocation uses `$skill-name`, not Claude slash commands.
Claude path/argument expansion and Claude Agent tool names are removed from active
procedures. References use explicit file paths rather than assuming macros.

The central root's skills are discoverable there. A separate project gets one
native bridge skill; central skill methods are read explicitly from its pinned
installation, not claimed as auto-discovered. No global settings have been altered.
This verifies format/path conformance and the CLI routing behavior, not live model
selection reliability in every Codex client. A new session is the manual smoke test:
open an initialized project, select founder-context, verify status and route.

Local tools default to Python 3.11+ for the new framework; upstream tools originally
targeted Python 3.8+. No dependencies are installed. GitHub Actions prepares a
Windows/Ubuntu 3.11/3.13 matrix; only the local Windows interpreter has run here.
