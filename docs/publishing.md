# Private GitHub publication

Requested name: `founder-os`. Description:
`A modular, AI-native Founder Operating System for building, managing and scaling projects with Codex.`

Git and gh are installed. The initial sandboxed `gh auth status` reported an invalid
token; an authorized check outside the restricted network confirmed valid keyring
authentication. The connected app has no repository-creation tool, so gh is the
available authorized fallback. Authenticated gh lookup found no repository at the
requested owner/name. The owner explicitly confirmed rights to all supplied content.

For later re-publication or recovery, first check from the local repository:

```powershell
gh auth status
gh repo view SimonKoesi/founder-os --json nameWithOwner,isPrivate,url
```

If the repository exists, STOP and inspect it; do not overwrite, force-push or
reuse it automatically. If lookup fails, verify the error is truly not-found
using the authenticated account, rather than permissions/network failure.
Only after confirming absence:

```powershell
python scripts/founder.py validate
python -m unittest discover -s tests -v
git status --short
git ls-files
# Review tracked files: .local and machine bindings must be absent.
gh repo create founder-os --private --description "A modular, AI-native Founder Operating System for building, managing and scaling projects with Codex." --source . --remote origin --push
gh repo view --json nameWithOwner,isPrivate,url
git ls-remote --heads origin main
gh run list --limit 5
```

The original request authorizes private creation; source-rights confirmation is
recorded in NOTICE. No new token belongs in shell arguments, files, chat, logs or
commits. Authentication stays in gh's
approved credential storage. Do not mark release/CI successful until remote evidence.
