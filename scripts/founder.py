#!/usr/bin/env python3
"""Founder OS: dependency-free project bootstrap, context routing and validation."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PHASES = ('discovery', 'validation', 'strategy', 'definition', 'planning', 'architecture',
          'design', 'implementation', 'testing', 'review', 'deployment', 'launch',
          'operation', 'optimization', 'scaling', 'archive')
STATUSES = ('active', 'blocked', 'complete', 'archived')
START = '<!-- founder-os:start -->'
END = '<!-- founder-os:end -->'

class FounderError(Exception):
    pass

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n'

def now():
    return datetime.now(timezone.utc).isoformat()

def runtime_files(root):
    manifest = read_json(root / 'framework.json')
    paths = []
    for item in manifest['runtime']:
        p = root / item
        if p.is_dir():
            paths.extend(x for x in p.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix != '.pyc')
        elif p.is_file():
            paths.append(p)
        else:
            raise FounderError('missing runtime member: ' + item)
    return sorted(set(paths))

def fingerprint(root):
    h = hashlib.sha256()
    for p in runtime_files(root):
        if p.is_symlink():
            raise FounderError('runtime symlink is not portable: ' + str(p))
        h.update(p.relative_to(root).as_posix().encode() + b'\0')
        # Git line-ending conversion must not invalidate portable content pins.
        h.update(p.read_bytes().replace(b'\r\n', b'\n') + b'\0')
    return h.hexdigest()

def safe_project(path):
    raw = Path(path).absolute()
    for ancestor in (raw, *raw.parents):
        if ancestor.is_symlink() or (hasattr(ancestor, 'is_junction') and ancestor.is_junction()):
            raise FounderError('refuse linked project path: ' + str(ancestor))
        if os.name == 'nt' and ancestor.exists():
            import stat
            if ancestor.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise FounderError('refuse Windows reparse point: ' + str(ancestor))
    return raw.resolve()

def safe_file(path):
    if path.is_symlink():
        raise FounderError('refuse linked managed file: ' + str(path))
    safe_project(path)

def atomic_text(path, text):
    safe_file(path)
    fd, tmp = tempfile.mkstemp(prefix='.founder-', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

@contextmanager
def project_lock(project):
    lock = project / '.founder-init.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise FounderError('project locked; inspect interrupted operation before removing .founder-init.lock')
    try:
        yield
    finally:
        lock.rmdir()

def bridge():
    return f'''{START}
## Founder OS

Read `.founder/project.json`, `.founder/state.json`, `.founder/context.md` and
`.founder/handoff.md` before project work. Preserve this project's existing rules.
Resolve the central framework from `FOUNDER_OS_HOME` or ignored
`.founder/local.json` (`framework_path`). If absent, ask for its local checkout;
never guess or download untrusted instructions. Run its `scripts/founder.py status
--project .` and verify version/digest before reading central modules.
Use its `route TASK --project .` to select skills, workflow and standards; then
explicitly read the returned central paths. They are not auto-loaded by links.
The local `founder-context` skill is a discovery bridge, not a framework copy.
Local exceptions belong in `.founder/decisions.md` with reason/revisit trigger.
Finish by updating project state and handoff with actual checks and next action.
{END}
'''

def project_data(name, kind, size, stack, framework):
    return {'schema_version': 1, 'name': name, 'type': kind, 'size': size, 'stack': stack,
            'framework': {'version': read_json(framework / 'framework.json')['version'],
                          'sha256': fingerprint(framework)}}

def bootstrap(args, adopt=False):
    project = safe_project(args.path)
    if project == ROOT or project in ROOT.parents or ROOT in project.parents:
        raise FounderError('project must be separate from the central framework')
    if not args.name.strip() or '\n' in args.name:
        raise FounderError('name must be a nonempty single line')
    if adopt and not project.is_dir():
        raise FounderError('adopt requires an existing project directory')
    if project.exists() and not project.is_dir():
        raise FounderError('target is not a directory')
    if not adopt and project.exists() and any(project.iterdir()):
        raise FounderError('target is not empty; use adopt to preserve an existing project')
    project.mkdir(parents=True, exist_ok=True)
    with project_lock(project):
        if (project / '.founder').exists():
            raise FounderError('project already has .founder; inspect status instead')
        profile = read_json(ROOT / 'project-types/profiles.json')[args.type]
        data = project_data(args.name, args.type, args.size, args.stack, ROOT)
        state = {'schema_version': 1, 'phase': 'discovery' if adopt else profile['phase'],
                 'status': 'active', 'updated_at': now(),
                 'tasks': [{'id':'T1', 'title':'Inspect existing project' if adopt else 'Define acceptance and evidence', 'status':'todo'}],
                 'risks': [], 'checks': [], 'next_action':'Inspect context and define the smallest verifiable outcome.'}
        files = {
            '.founder/project.json': json_text(data), '.founder/state.json': json_text(state),
            '.founder/local.json': json_text({'framework_path': str(ROOT)}),
            '.founder/context.md': f'# {args.name}\n\nPurpose, users, requirements and acceptance: to be established from owner evidence.\n\nFocus: ' + ', '.join(profile['focus']) + '.\n\nChecks: ' + ', '.join(profile['checks']) + '.\n',
            '.founder/roadmap.md': '# Roadmap\n\nNext outcome: agree on the problem and a verifiable first slice.\n',
            '.founder/decisions.md': '# Decisions\n\nFramework binding recorded in project.json. Add significant rationale here.\n',
            '.founder/handoff.md': '# Handoff\n\nBootstrap complete. No product implementation or project tests have run.\nRead context, inspect the actual tree and execute the first discovery task.\n',
            '.agents/skills/founder-context/SKILL.md': '''---
name: founder-context
description: Resume a Founder OS project and route its business, product, software or operations task to the pinned central framework.
---
Read project AGENTS and `.founder/project.json`, `state.json`, `context.md`,
`handoff.md`. Resolve central path using FOUNDER_OS_HOME or .founder/local.json.
Verify pin with its scripts/founder.py status --project .; then route the task.
Read only selected central skill/workflow/standards by explicit file path.
If central files are inaccessible, report the missing dependency and continue
only work supported by local project evidence. Do not silently use a different version.
'''}
        for rel in files:
            p = project / rel
            safe_file(p)
            if p.exists():
                raise FounderError('would overwrite existing file: ' + rel)
        changes = {}
        for rel in ('AGENTS.md', '.gitignore'):
            p = project / rel
            safe_file(p)
            changes[rel] = p.read_bytes() if p.exists() else None
        agents = (changes['AGENTS.md'] or b'').decode('utf-8-sig')
        if START in agents or END in agents:
            raise FounderError('existing Founder OS marker; manual inspection required')
        files['AGENTS.md'] = agents.rstrip() + '\n\n' + bridge()
        ignores = (changes['.gitignore'] or b'').decode('utf-8-sig')
        files['.gitignore'] = ignores.rstrip() + '\n\n# Founder OS machine-local files\n.founder/local.json\n.founder/history/\n.founder-init.lock/\n'
        # No src/tests scaffold: the actual stack creates useful source directories.
        written = []
        try:
            for rel, text in files.items():
                p = project / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                atomic_text(p, text)
                written.append(rel)
            problems = validate_project(project)
            if problems:
                raise FounderError('; '.join(problems))
        except Exception:
            for rel in reversed(written):
                p = project / rel
                if rel in changes and changes[rel] is not None:
                    p.write_bytes(changes[rel])
                elif p.exists():
                    p.unlink()
            for p in sorted({(project / rel).parent for rel in files}, key=lambda x: len(x.parts), reverse=True):
                while p != project and p.exists() and not any(p.iterdir()):
                    p.rmdir()
                    p = p.parent
            raise
    return {'project':str(project), 'action':'adopted' if adopt else 'initialized', 'framework':data['framework']}

def validate_project(project):
    errors = []
    try:
        for name in ('project.json', 'state.json', 'context.md', 'handoff.md', 'decisions.md', 'roadmap.md'):
            p = project / '.founder' / name
            safe_file(p)
            if not p.is_file() or not p.read_text(encoding='utf-8').strip():
                errors.append('missing/empty .founder/' + name)
        p = read_json(project / '.founder/project.json')
        s = read_json(project / '.founder/state.json')
        profiles = read_json(ROOT / 'project-types/profiles.json')
        if p.get('schema_version') != 1 or s.get('schema_version') != 1:
            errors.append('unsupported project/state schema')
        if not isinstance(p.get('name'), str) or not p['name'].strip():
            errors.append('project name required')
        if p.get('type') not in profiles or p.get('size') not in ('small', 'standard', 'large'):
            errors.append('invalid type or size')
        if not isinstance(p.get('stack'), list) or any(not isinstance(x, str) for x in p['stack']):
            errors.append('stack must be a string list')
        pin = p.get('framework', {})
        if not re.fullmatch(r'\d+\.\d+\.\d+', str(pin.get('version', ''))) or not re.fullmatch('[a-f0-9]{64}', str(pin.get('sha256', ''))):
            errors.append('invalid framework pin')
        if s.get('phase') not in PHASES or s.get('status') not in STATUSES:
            errors.append('invalid phase or status')
        if not isinstance(s.get('next_action'), str) or not s['next_action'].strip():
            errors.append('next_action required')
        try:
            datetime.fromisoformat(s['updated_at'])
        except (KeyError, TypeError, ValueError):
            errors.append('updated_at must be ISO date/time')
        for key in ('tasks', 'risks', 'checks'):
            if not isinstance(s.get(key), list):
                errors.append(key + ' must be a list')
        ids = set()
        for t in s.get('tasks', []) if isinstance(s.get('tasks'), list) else []:
            if not isinstance(t, dict) or not isinstance(t.get('id'), str) or not t['id'] or not t.get('title') or t.get('status') not in ('todo','doing','done','blocked'):
                errors.append('invalid task')
                continue
            if t['id'] in ids:
                errors.append('duplicate task id: ' + t['id'])
            ids.add(t['id'])
        for c in s.get('checks', []) if isinstance(s.get('checks'), list) else []:
            if not isinstance(c, dict) or not c.get('command') or c.get('result') not in ('passed','failed','not-run') or not c.get('at'):
                errors.append('invalid check')
        if not (project / 'AGENTS.md').is_file() or START not in (project / 'AGENTS.md').read_text(encoding='utf-8-sig'):
            errors.append('missing AGENTS bridge')
    except (OSError, ValueError, TypeError, AttributeError, FounderError) as e:
        errors.append('invalid context: ' + str(e))
    return errors

def central_path(project):
    env = os.environ.get('FOUNDER_OS_HOME')
    if env:
        return Path(env).resolve()
    local = project / '.founder/local.json'
    if not local.is_file():
        raise FounderError('missing machine binding; use bind --framework PATH')
    return Path(read_json(local)['framework_path']).resolve()

def status(project):
    problems = validate_project(project)
    if problems:
        raise FounderError('; '.join(problems))
    data = read_json(project / '.founder/project.json')
    central = central_path(project)
    found = {'version':read_json(central / 'framework.json')['version'], 'sha256':fingerprint(central)}
    if data['framework'] != found:
        raise FounderError('framework pin mismatch; bind matching installation or explicitly update after review')
    state = read_json(project / '.founder/state.json')
    return {'project':data['name'], 'framework':found, 'phase':state['phase'], 'status':state['status'],
            'next_action':state['next_action'], 'risks':state['risks'], 'checks':state['checks']}

def route(task, project=None):
    routes = read_json(ROOT / 'core/routes.json')
    text = task.casefold()
    matches = [dict(r, reason='explicit id/keyword') for r in routes
               if r['id'] == text or any(k.casefold() in text for k in r['keywords'])]
    if project:
        st = status(project)
        for r in routes:
            if st['phase'] in r['phases'] and r['id'] not in {x['id'] for x in matches}:
                matches.append(dict(r, reason='current phase: ' + st['phase']))
    if not matches:
        matches = [dict(routes[0], reason='unclassified: discovery fallback')]
    return {'task':task, 'routes':matches, 'note':'Review semantic fit; keyword matching is advisory. Paths are relative to central framework.'}

def update(project, framework, apply=False, bind=False):
    problems = validate_project(project)
    if problems:
        raise FounderError('; '.join(problems))
    path = project / '.founder/project.json'
    data = read_json(path)
    manifest = read_json(framework / 'framework.json')
    if manifest['project_schema'] != data['schema_version']:
        raise FounderError('schema migration required; no files changed')
    new = {'version':manifest['version'], 'sha256':fingerprint(framework)}
    old = data['framework']
    if bind and old != new:
        raise FounderError('bind requires exact pinned version/digest; use update for deliberate upgrades')
    result = {'old':old, 'new':new, 'applied':False, 'project_content_changed':False}
    if apply or bind:
        with project_lock(project):
            # Optimistic concurrency check before mutation.
            if read_json(path) != data:
                raise FounderError('project changed during update; retry after inspection')
            local = project / '.founder/local.json'
            safe_file(local)
            previous_local = local.read_bytes() if local.exists() else None
            original = path.read_bytes()
            backup = None
            if old != new:
                history = project / '.founder/history'
                safe_project(history)
                history.mkdir(exist_ok=True)
                backup = history / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f') + '-project.json')
                backup.write_bytes(original)
            try:
                atomic_text(local, json_text({'framework_path':str(framework)}))
                if not bind and old != new:
                    data['framework'] = new
                    atomic_text(path, json_text(data))
            except Exception:
                atomic_text(path, original.decode('utf-8-sig'))
                if previous_local is None:
                    local.unlink(missing_ok=True)
                else:
                    atomic_text(local, previous_local.decode('utf-8-sig'))
                raise
            result.update(applied=True, backup=str(backup) if backup else None)
    return result

def install(destination):
    dest = safe_project(destination)
    if dest.exists():
        raise FounderError('install destination already exists; choose a new version directory')
    if dest == ROOT or ROOT in dest.parents or dest in ROOT.parents:
        raise FounderError('installation must be separate from source checkout')
    dest.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.founder-install-', dir=dest.parent))
    try:
        for p in runtime_files(ROOT):
            target = staging / p.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, target)
        for name in ('LICENSE','NOTICE.md'):
            shutil.copyfile(ROOT / name, staging / name)
        if fingerprint(staging) != fingerprint(ROOT):
            raise FounderError('installation verification failed')
        staging.rename(dest)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return {'installation':str(dest), 'sha256':fingerprint(dest)}

def markdown_links(path):
    text = path.read_text(encoding='utf-8-sig')
    text = re.sub(r'(?ms)^\s*(```|~~~).*?^\s*\1\s*$', '', text)
    for value in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        value = value.split(' "', 1)[0].strip('<>')
        if not value or value.startswith(('#','http:','https:','mailto:','plugin:','app:')):
            continue
        yield (path.parent / unquote(value.split('#', 1)[0])).resolve()

def validate(root=ROOT):
    errors = []
    files = [p for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in ('.git','.local','__pycache__','.venv'))]
    for p in files:
        if p.suffix == '.md':
            for target in markdown_links(p):
                if not target.is_file():
                    errors.append(f'broken link: {p.relative_to(root)} -> {target.name}')
    skills = root / '.agents/skills'
    for p in skills.glob('*/SKILL.md'):
        text = p.read_text(encoding='utf-8')
        m = re.match(r'^---\nname: ([a-z0-9-]{1,63})\ndescription: (.+)\n---\n', text)
        if not m or m[1] != p.parent.name:
            errors.append('invalid skill frontmatter/name: ' + str(p.relative_to(root)))
        if '${CLAUDE_SKILL_DIR}' in text or '$ARGUMENTS' in text:
            errors.append('unexpanded Claude syntax: ' + str(p.relative_to(root)))
    ids = set()
    for r in read_json(root / 'core/routes.json'):
        if r['id'] in ids:
            errors.append('duplicate route: ' + r['id'])
        ids.add(r['id'])
        if any(x not in PHASES for x in r['phases']):
            errors.append('invalid route phase: ' + r['id'])
        for key in ('skills','standards','workflows'):
            for rel in r[key]:
                if not (root / rel).is_file():
                    errors.append('missing route target: ' + rel)
    mapping = root / 'docs/migration/source-to-target.json'
    if mapping.is_file():
        entries = read_json(mapping)
        seen = set()
        for e in entries:
            if e['source'] in seen or not e['targets'] or e['status'] != 'read-completely':
                errors.append('incomplete/duplicate source mapping: ' + e['source'])
            seen.add(e['source'])
            for rel in e['targets']:
                if not (root / rel).is_file():
                    errors.append('missing migration target: ' + rel)
            archive = root / '.local/source' / e['source']
            if archive.exists() and hashlib.sha256(archive.read_bytes()).hexdigest() != e['sha256']:
                errors.append('source archive hash mismatch: ' + e['source'])
    # Match values, never print secret-bearing lines.
    patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'AKIA[0-9A-Z]{16}',
                r'sk-(?:proj-)?[A-Za-z0-9_-]{32,}', r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----']
    for p in files:
        if p.suffix not in ('.py','.json','.md','.yml','.yaml','.toml',''):
            continue
        text = p.read_text(encoding='utf-8-sig')
        if any(re.search(pattern, text) for pattern in patterns):
            errors.append('possible secret in: ' + str(p.relative_to(root)))
    for p in root.glob('examples/*/.founder/project.json'):
        errors.extend(validate_project(p.parents[1]))
    fingerprint(root)
    return errors

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='cmd', required=True)
    profiles = read_json(ROOT / 'project-types/profiles.json')
    for cmd in ('init','adopt'):
        p = sub.add_parser(cmd)
        p.add_argument('path')
        p.add_argument('--name', required=True)
        p.add_argument('--type', choices=profiles, default='software')
        p.add_argument('--size', choices=('small','standard','large'), default='small')
        p.add_argument('--stack', nargs='*', default=[])
    p = sub.add_parser('route')
    p.add_argument('task')
    p.add_argument('--project')
    for cmd in ('status','validate','update','bind'):
        p = sub.add_parser(cmd)
        p.add_argument('--project', required=cmd not in ('validate',))
        if cmd in ('update','bind'):
            p.add_argument('--framework', required=True)
            if cmd == 'update':
                p.add_argument('--apply', action='store_true')
    p = sub.add_parser('install')
    p.add_argument('destination')
    sub.add_parser('fingerprint')
    args = parser.parse_args(argv)
    try:
        if args.cmd in ('init','adopt'):
            result = bootstrap(args, args.cmd == 'adopt')
        elif args.cmd == 'route':
            result = route(args.task, safe_project(args.project) if args.project else None)
        elif args.cmd == 'status':
            result = status(safe_project(args.project))
        elif args.cmd == 'validate':
            errors = validate_project(safe_project(args.project)) if args.project else validate()
            print(json_text({'ok':not errors, 'errors':errors}), end='')
            return 1 if errors else 0
        elif args.cmd in ('update','bind'):
            result = update(safe_project(args.project), Path(args.framework).resolve(),
                            getattr(args,'apply',False), args.cmd == 'bind')
        elif args.cmd == 'install':
            result = install(args.destination)
        else:
            result = {'sha256':fingerprint(ROOT)}
        print(json_text(result), end='')
        return 0
    except (FounderError, OSError, ValueError, KeyError, TypeError) as e:
        print('error: ' + str(e), file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
