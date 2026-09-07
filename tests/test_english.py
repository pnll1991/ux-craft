from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EnglishEditionTests(unittest.TestCase):
    def test_main_readme_is_english_first(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Build with intent", text)
        self.assertIn("README.es.md", text)

    def test_skill_version(self):
        text = (ROOT / "skills/ux-craft/SKILL.md").read_text(encoding="utf-8")
        self.assertIn('version: "1.0.1"', text)

    def test_demo_is_local_only(self):
        text = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertNotIn("https://", text.split("<script>", 1)[-1])
        self.assertIn("30 principles", text.lower())


if __name__ == "__main__":
    unittest.main()
