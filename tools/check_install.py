#!/usr/bin/env python3
"""End-to-end install / update / uninstall check of the plugin with the Claude Code CLI.

Runs in a throwaway copy of the repository and a throwaway Claude Code config
directory (CLAUDE_CONFIG_DIR), so nothing of the user's setup is touched:

  1. claude plugin marketplace add <copy>        -> marketplace "ecommerce-skills"
  2. claude plugin install ecommerce-skills@ecommerce-skills
  3. claude plugin details                       -> version and "Skills (N)" == manifest
  4. bump the version in the copy's marketplace.json (simulated release)
  5. claude plugin marketplace update + claude plugin update -> new version installed
  6. claude plugin uninstall + marketplace remove

Usage:
  python3 tools/check_install.py                    # uses `claude` from PATH
  python3 tools/check_install.py /path/to/claude    # explicit CLI
Exit code 0 when every step passes. Standard library only. No API call is made.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cli, args, env):
    r = subprocess.run([cli, *args], capture_output=True, text=True, env=env, timeout=180)
    return r.returncode, r.stdout + r.stderr


def main():
    cli = sys.argv[1] if len(sys.argv) > 1 else shutil.which("claude")
    if not cli:
        print("SKIP: Claude Code CLI not found")
        return 0
    manifest = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = manifest["plugins"][0]
    expected_skills, version = len(plugin["skills"]), plugin["version"]
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / "repo"
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__", "results"))
        env = {**os.environ, "CLAUDE_CONFIG_DIR": str(Path(tmp) / "config"), "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"}
        pid = f"{plugin['name']}@{manifest['name']}"

        def step(label, args, check=None):
            nonlocal ok
            code, out = run(cli, args, env)
            passed = code == 0 and (check(out) if check else True)
            ok &= passed
            print(f"{'PASS' if passed else 'FAIL'}  {label}")
            if not passed:
                print("      " + out.strip().replace("\n", "\n      ")[:800])
            return out

        step("marketplace add", ["plugin", "marketplace", "add", str(copy)])
        step("plugin install", ["plugin", "install", pid])
        step(f"details: version {version} and {expected_skills} skills", ["plugin", "details", pid],
             lambda o: f"{plugin['name']} {version}" in o and f"Skills ({expected_skills})" in o)

        # Simulated release: bump the patch number in the copy
        major, minor, patch = (re.findall(r"\d+", version) + ["0", "0", "0"])[:3]
        new_version = f"{major}.{minor}.{int(patch) + 1}"
        m = json.loads((copy / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        m["plugins"][0]["version"] = m["metadata"]["version"] = new_version
        (copy / ".claude-plugin" / "marketplace.json").write_text(json.dumps(m, indent=2), encoding="utf-8")
        step("marketplace update", ["plugin", "marketplace", "update", manifest["name"]])
        step(f"plugin update to {new_version}", ["plugin", "update", pid])
        step(f"details after update: version {new_version}", ["plugin", "details", pid],
             lambda o: f"{plugin['name']} {new_version}" in o)
        step("plugin uninstall", ["plugin", "uninstall", pid])
        step("marketplace remove", ["plugin", "marketplace", "remove", manifest["name"]])
    print("OK: install, update and uninstall work" if ok else "FAILED: see steps above")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
