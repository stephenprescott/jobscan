"""Install the pre-push privacy check for maintainers of this repo.

Usage: python scripts/install_hooks.py
Then set JOBSCAN_DENYLIST to the path of your private denylist file
(one term per line, kept OUTSIDE this repo). Pushes fail while it is unset.
"""
from pathlib import Path

HOOK = """#!/bin/sh
# jobscan privacy check: blocks a push if personal data is found.
if [ -z "$JOBSCAN_DENYLIST" ]; then
  echo "Push blocked: set JOBSCAN_DENYLIST to your private denylist file." >&2
  exit 1
fi
python scripts/privacy_scan.py . --denylist "$JOBSCAN_DENYLIST" || exit 1
git log -p --format=%B | python scripts/privacy_scan.py - --denylist "$JOBSCAN_DENYLIST" || exit 1
"""


def install(repo: Path) -> Path:
    hook = Path(repo) / ".git" / "hooks" / "pre-push"
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text(HOOK, encoding="utf-8", newline="\n")
    hook.chmod(0o755)
    return hook


if __name__ == "__main__":
    print(f"Installed {install(Path(__file__).resolve().parent.parent)}")
