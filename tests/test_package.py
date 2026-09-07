from pathlib import Path
import importlib.util
import json
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


validate = load_module(ROOT / "scripts/validate.py", "ux_validate")
install = load_module(ROOT / "scripts/install.py", "ux_install")


class PackageTests(unittest.TestCase):
    def test_validation_passes(self):
        self.assertEqual(validate.validate(), [])

    def test_catalog_has_30_unique_principles(self):
        data = json.loads((ROOT / "skills/ux-craft/references/principles.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data), 30)
        self.assertEqual(len({item["id"] for item in data}), 30)

    def test_installer_copies_skill_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            dest = install.install("codex", base)
            self.assertTrue((dest / "SKILL.md").is_file())
            self.assertTrue((dest / "references/principles.md").is_file())
            with self.assertRaises(FileExistsError):
                install.install("codex", base)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            destination = install.install("cursor", base, dry_run=True)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
