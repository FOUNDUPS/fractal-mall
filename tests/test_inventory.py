"""Exercise the public inventory command against an isolated Git repository."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class InventoryTest(unittest.TestCase):
    def test_inventory_uses_the_requested_tree(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "notebook"
            tools = root / "tools"
            tools.mkdir(parents=True)
            script = tools / "inventory.py"
            shutil.copyfile(Path(__file__).resolve().parents[1] / "tools" / script.name, script)

            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args])

            git("init", "--quiet")
            names = ["case A.md", "case\tB.md"]
            for name in names:
                (root / name).write_bytes(b"one component\n")
            git("add", ".")
            git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "--quiet", "-m", "freeze fixture")
            commit = git("rev-parse", "HEAD").decode().strip()
            (root / names[0]).write_text("working copy edit")
            (root / "scratch.md").write_text("untracked")
            command = [sys.executable, str(script), commit]
            first = subprocess.check_output(command, cwd=temporary)
            self.assertEqual(first, subprocess.check_output(command, cwd=temporary))
            manifest = json.loads(first)
            self.assertEqual(manifest["commit"], commit)
            self.assertEqual(manifest["entry_count"], 3)
            paths = {entry["path"]: entry for entry in manifest["entries"]}
            self.assertEqual(set(paths), {*names, "tools/inventory.py"})
            for path, entry in paths.items():
                expected = git("rev-parse", f"{commit}:{path}").decode().strip()
                self.assertEqual(entry["object_id"], expected)
                self.assertEqual(entry["type"], "blob")
            self.assertEqual(paths[names[0]]["object_id"], paths[names[1]]["object_id"])
            bad = subprocess.run([sys.executable, str(script), "missing-revision"],
                                 cwd=temporary, capture_output=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertEqual(bad.stdout, b"")
