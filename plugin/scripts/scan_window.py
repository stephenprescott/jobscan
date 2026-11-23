"""Work out a scan's time window and each job board's date filter.

Usage:
  python -I scan_window.py <jobscan.config.md>                 print the window as JSON
  python -I scan_window.py <jobscan.config.md> --mark-success  record a complete scan (now)

Reads `window` (since_last | 24h), `window_cap_days` and `last_successful_scan`
from the config's front matter. Standard library only.
"""
import json
import math
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

INDEED_DAYS = [1, 3, 7, 14]


def window_start(now: datetime, window: str, last, cap_days: int) -> datetime:
    if window == "24h":
        return now - timedelta(hours=24)
    floor = now - timedelta(days=cap_days)
    return last if last is not None and last > floor else floor


def board_filters(now: datetime, start: datetime) -> dict:
    span = now - start
    days = span.total_seconds() / 86400
    return {
        "start": start.isoformat(),
        "linkedin_f_TPR": f"r{math.ceil(span.total_seconds())}",
        "indeed_fromage": next((d for d in INDEED_DAYS if d >= days - 1e-9), INDEED_DAYS[-1]),
        "google_tbs": "qdr:d" if days <= 1 else "qdr:w",
    }


def _front(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("jobscan.config.md has no settings block. Run /jobscan:setup.")
    return m.group(1)


def _value(front: str, key: str):
    m = re.search(rf"^{key}:[ \t]*(.*)$", front, re.M)
    v = m.group(1).strip().strip("'\"") if m else ""
    return None if v in ("", "null", "~") else v


def read_settings(path: Path):
    front = _front(Path(path).read_text(encoding="utf-8"))
    window = _value(front, "window") or "24h"
    cap = int(_value(front, "window_cap_days") or 3)
    last = _value(front, "last_successful_scan")
    last = datetime.fromisoformat(last) if last else None
    if last is not None and last.tzinfo is None:
        last = last.replace(tzinfo=timezone.utc)
    return window, cap, last


def mark_success(path: Path, now: datetime) -> None:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"^last_successful_scan:.*$", f"last_successful_scan: '{now.isoformat()}'",
                 text, count=1, flags=re.M)
    path.write_text(new, encoding="utf-8", newline="")


def main(argv=None) -> None:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        sys.exit(__doc__)
    cfg = Path(args[0])
    now = datetime.now(timezone.utc).replace(microsecond=0)
    if "--mark-success" in args[1:]:
        mark_success(cfg, now)
        print(f"last_successful_scan set to {now.isoformat()}")
        return
    window, cap, last = read_settings(cfg)
    out = board_filters(now, window_start(now, window, last, cap))
    out["window"] = window
    print(json.dumps(out))


if __name__ == "__main__":
    main()
