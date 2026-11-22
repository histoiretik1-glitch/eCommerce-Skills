"""Shared helpers for the plugin test suite (standard library only)."""
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GOLDEN = Path(__file__).resolve().parent / "golden"

# Lines whose content depends on the current date/time
_DATE_LINE = re.compile(
    r"(\d{4}-\d{2}-\d{2}|\d{4}years|(January|February|March|April|May|June|July|August|"
    r"September|October|November|December) \d{1,2}, \d{4})"
)


def strip_dates(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not _DATE_LINE.search(line))


def run_script(skill_dir: Path, script: str, *args: str, cwd: Path = None):
    """Run scripts/<script> of a skill, from its folder by default. Returns CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(skill_dir / "scripts" / script), *args],
        cwd=str(cwd or skill_dir), capture_output=True, text=True, timeout=60,
    )


def load_module(path: Path, name: str):
    """Import a script as a module under a unique name (its folder goes first on sys.path)."""
    sys.path.insert(0, str(path.parent))
    try:
        for cached in ("templates", "calculator", "analyzer", "parser"):
            sys.modules.pop(cached, None)
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


def golden(name: str) -> str:
    return (GOLDEN / name).read_text(encoding="utf-8")
