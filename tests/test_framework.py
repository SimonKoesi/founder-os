import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('founder_cli', ROOT / 'scripts/founder.py')
fw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fw)

class Framework(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.project = self.base / 'project with spaces'

    def tearDown(self):
        self.tmp.cleanup()

    def args(self, kind='software'):
        return argparse.Namespace(path=str(self.project), name='Demo', type=kind, size='small', stack=[])

    def test_new_idea_and_resume(self):
        fw.bootstrap(self.args('idea'))
        self.assertEqual(fw.status(self.project)['phase'], 'discovery')
        self.assertEqual(fw.validate_project(self.project), [])
        route = fw.route('Neue Geschäftsidee prüfen', self.project)
        self.assertIn('discovery', [x['id'] for x in route['routes']])
        self.assertTrue((self.project / '.founder/handoff.md').is_file())
        self.assertFalse((self.project / 'src').exists())

    def test_saas_and_automation(self):
        for kind in ('saas','automation'):
            self.project = self.base / kind
            fw.bootstrap(self.args(kind))
            context = (self.project / '.founder/context.md').read_text(encoding='utf-8')
            self.assertIn('tenant isolation' if kind == 'saas' else 'duplicate trigger', context)
            self.assertEqual(fw.status(self.project)['phase'], 'definition')

    def test_adopt_preserves_code_rules_and_ignores(self):
        self.project.mkdir()
        (self.project / 'app.py').write_bytes(b'user data and code')
        (self.project / 'AGENTS.md').write_text('# Local\nKeep IDs.', encoding='utf-8')
        (self.project / '.gitignore').write_text('private/\n', encoding='utf-8')
        fw.bootstrap(self.args(), adopt=True)
        self.assertEqual((self.project / 'app.py').read_bytes(), b'user data and code')
        self.assertTrue((self.project / 'AGENTS.md').read_text().startswith('# Local\nKeep IDs.'))
        self.assertTrue((self.project / '.gitignore').read_text().startswith('private/'))
        before = (self.project / 'AGENTS.md').read_bytes()
        with self.assertRaises(fw.FounderError):
            fw.bootstrap(self.args(), adopt=True)
        self.assertEqual((self.project / 'AGENTS.md').read_bytes(), before)

    def test_nonempty_init_and_collision_do_not_change_existing(self):
        self.project.mkdir()
        (self.project / 'README.md').write_text('existing')
        with self.assertRaises(fw.FounderError):
            fw.bootstrap(self.args())
        p = self.project / '.agents/skills/founder-context/SKILL.md'
        p.parent.mkdir(parents=True)
        p.write_text('custom')
        with self.assertRaises(fw.FounderError):
            fw.bootstrap(self.args(), adopt=True)
        self.assertFalse((self.project / '.founder').exists())
        self.assertEqual(p.read_text(), 'custom')

    def test_failure_rolls_back_and_retry_works(self):
        self.project.mkdir()
        (self.project / 'AGENTS.md').write_bytes(b'# Existing\r\n')
        original = fw.atomic_text
        def fail(path, text):
            if path.name == 'state.json':
                raise OSError('isolated injected disk failure')
            original(path, text)
        with patch.object(fw, 'atomic_text', side_effect=fail):
            with self.assertRaises(OSError):
                fw.bootstrap(self.args(), adopt=True)
        self.assertFalse((self.project / '.founder').exists())
        self.assertEqual((self.project / 'AGENTS.md').read_bytes(), b'# Existing\r\n')
        self.assertFalse((self.project / '.founder-init.lock').exists())
        fw.bootstrap(self.args(), adopt=True)
        self.assertEqual(fw.status(self.project)['status'], 'active')

    def test_interrupted_lock_refused_without_writes(self):
        self.project.mkdir()
        (self.project / '.founder-init.lock').mkdir()
        with self.assertRaises(fw.FounderError):
            fw.bootstrap(self.args(), adopt=True)
        self.assertFalse((self.project / '.founder').exists())

    def test_update_preview_apply_and_bind_second_computer(self):
        fw.bootstrap(self.args())
        other = self.base / 'release 2'
        fw.install(other)
        with self.assertRaises(fw.FounderError):
            fw.install(other)
        fw.update(self.project, other, bind=True)
        self.assertEqual(fw.status(self.project)['status'], 'active')
        context = (self.project / '.founder/context.md').read_bytes()
        manifest = fw.read_json(other / 'framework.json')
        manifest['version'] = '1.1.0'
        (other / 'framework.json').write_text(fw.json_text(manifest))
        with self.assertRaises(fw.FounderError):
            fw.status(self.project)
        before = (self.project / '.founder/project.json').read_bytes()
        result = fw.update(self.project, other)
        self.assertFalse(result['applied'])
        self.assertEqual((self.project / '.founder/project.json').read_bytes(), before)
        with self.assertRaises(fw.FounderError):
            fw.update(self.project, other, bind=True)
        result = fw.update(self.project, other, apply=True)
        self.assertTrue(Path(result['backup']).is_file())
        self.assertEqual(fw.status(self.project)['framework']['version'], '1.1.0')
        self.assertEqual((self.project / '.founder/context.md').read_bytes(), context)
        # Restore prior metadata and bind the old release: deliberate rollback.
        shutil.copyfile(result['backup'], self.project / '.founder/project.json')
        fw.update(self.project, ROOT, bind=True)
        self.assertEqual(fw.status(self.project)['framework']['version'], '1.0.0')

    def test_schema_mismatch_and_state_errors(self):
        fw.bootstrap(self.args())
        p = self.project / '.founder/state.json'
        state = fw.read_json(p)
        state['tasks'].append(state['tasks'][0])
        state['phase'] = 'invented'
        p.write_text(fw.json_text(state))
        self.assertIn('invalid phase or status', fw.validate_project(self.project))
        self.assertTrue(any('duplicate task' in x for x in fw.validate_project(self.project)))

    def test_bugfix_and_all_route_targets(self):
        self.assertIn('bugfix', [r['id'] for r in fw.route('Fehler beheben')['routes']])
        for r in fw.read_json(ROOT / 'core/routes.json'):
            routed = fw.route(r['id'])
            self.assertIn(r['id'], [x['id'] for x in routed['routes']])
            for key in ('skills','workflows','standards'):
                self.assertTrue(all((ROOT / p).is_file() for p in r[key]))

    def test_cli_status_error_and_real_entrypoint(self):
        cmd = [sys.executable, str(ROOT / 'scripts/founder.py')]
        fail = subprocess.run(cmd + ['status','--project',str(self.project)], capture_output=True)
        self.assertEqual(fail.returncode, 2)
        good = subprocess.run(cmd + ['init',str(self.project),'--name','CLI','--type','automation'], capture_output=True)
        self.assertEqual(good.returncode, 0, good.stderr)
        status = subprocess.run(cmd + ['status','--project',str(self.project)], capture_output=True)
        self.assertEqual(json.loads(status.stdout)['project'], 'CLI')

    def test_missing_binding_and_wrong_environment_pin(self):
        fw.bootstrap(self.args())
        (self.project / '.founder/local.json').unlink()
        with self.assertRaises(fw.FounderError):
            fw.status(self.project)
        fw.update(self.project, ROOT, bind=True)
        self.assertEqual(fw.status(self.project)['status'], 'active')

    def test_runtime_line_endings_portable(self):
        other = self.base / 'release'
        fw.install(other)
        p = other / 'AGENTS.md'
        p.write_bytes(p.read_bytes().replace(b'\n', b'\r\n'))
        self.assertEqual(fw.fingerprint(other), fw.fingerprint(ROOT))

    def test_installation_is_self_contained(self):
        other = self.base / 'release'
        fw.install(other)
        self.assertEqual(fw.validate(other), [])
        result = subprocess.run([sys.executable, str(other / 'scripts/founder.py'),
                                 'init', str(self.project), '--name','Offline'], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(fw.status(self.project)['project'], 'Offline')

    def test_update_schema_refusal_and_failure_rollback(self):
        fw.bootstrap(self.args())
        other = self.base / 'release'
        fw.install(other)
        manifest = fw.read_json(other / 'framework.json')
        manifest['project_schema'] = 2
        (other / 'framework.json').write_text(fw.json_text(manifest))
        before = (self.project / '.founder/project.json').read_bytes()
        with self.assertRaises(fw.FounderError):
            fw.update(self.project, other, apply=True)
        self.assertEqual((self.project / '.founder/project.json').read_bytes(), before)
        manifest['project_schema'] = 1
        manifest['version'] = '1.1.0'
        (other / 'framework.json').write_text(fw.json_text(manifest))
        local_before = (self.project / '.founder/local.json').read_bytes()
        original = fw.atomic_text
        failed = False
        def fail_once(path, text):
            nonlocal failed
            if path.name == 'project.json' and not failed:
                failed = True
                raise OSError('isolated metadata write failure')
            original(path, text)
        with patch.object(fw, 'atomic_text', side_effect=fail_once):
            with self.assertRaises(OSError):
                fw.update(self.project, other, apply=True)
        self.assertEqual((self.project / '.founder/project.json').read_bytes(), before)
        self.assertEqual((self.project / '.founder/local.json').read_bytes(), local_before)

    def test_symlink_target_refused(self):
        real = self.base / 'real'
        real.mkdir()
        try:
            self.project.symlink_to(real, target_is_directory=True)
        except OSError:
            self.skipTest('Windows symlink creation requires unavailable privilege')
        with self.assertRaises(fw.FounderError):
            fw.bootstrap(self.args(), adopt=True)
        self.assertEqual(list(real.iterdir()), [])

    def test_validator_catches_broken_link(self):
        p = self.base / 'doc.md'
        p.write_text('[broken](missing.md)\n```\n[example](ignore.md)\n```\n')
        self.assertEqual(list(fw.markdown_links(p)), [self.base / 'missing.md'])

    def test_repository_integrity(self):
        self.assertEqual(fw.validate(), [])

if __name__ == '__main__':
    unittest.main()
