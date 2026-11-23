"""Scan files for personal data before anything is pushed.

Usage: python scripts/privacy_scan.py <root | -> --denylist <file>
  <root>  folder to scan, or "-" to scan text from stdin (e.g. `git log -p`)
Exit 0 when clean, 1 when anything matches.
"""
import argparse
import re
import sys
from collections import namedtuple
from pathlib import Path

Finding = namedtuple("Finding", "path line term")

SKIP_DIRS = {".git", ".superpowers", "__pycache__", ".pytest_cache"}
PATTERNS = [
    ("phone number", re.compile(r"(?<!\d)\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)")),
    ("claude artifact link", re.compile(r"claude\.ai/(?:code/)?artifact/[A-Za-z0-9-]+")),
    ("email address", re.compile(r"[\w.+-]+@(?!example\.(?:com|org)\b)[\w-]+(?:\.[\w-]+)+")),
]


def load_denylist(path) -> list[str]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]


def scan_text(text: str, name: str, denylist: list[str]) -> list[Finding]:
    found = []
    terms = [(t, t.lower()) for t in denylist]
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        found += [Finding(name, n, t) for t, tl in terms if tl in low]
        found += [Finding(name, n, label) for label, rx in PATTERNS if rx.search(line)]
    return found


def scan(root: Path, denylist: list[str]) -> list[Finding]:
    root = Path(root)
    found = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if not p.is_file() or SKIP_DIRS.intersection(rel.parts):
            continue
        data = p.read_bytes()
        if b"\x00" in data[:8192]:
            continue
        found += scan_text(data.decode("utf-8", errors="replace"), rel.as_posix(), denylist)
    return found


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root")
    ap.add_argument("--denylist", required=True)
    a = ap.parse_args(argv)
    deny = load_denylist(a.denylist)
    found = scan_text(sys.stdin.read(), "<stdin>", deny) if a.root == "-" else scan(Path(a.root), deny)
    for f in found:
        print(f"{f.path}:{f.line}: {f.term}")
    print(f"{len(found)} finding(s)" if found else "clean")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
