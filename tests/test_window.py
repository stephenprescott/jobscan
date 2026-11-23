import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import scan_window
from scan_window import board_filters, mark_success, window_start

NOW = datetime(2026, 12, 10, 9, 0, tzinfo=timezone.utc)
TEMPLATE = Path(__file__).resolve().parent.parent / "plugin" / "templates" / "jobscan.config.md"


def test_24h_always_24h():
    last = NOW - timedelta(hours=5)
    assert window_start(NOW, "24h", last, 3) == NOW - timedelta(hours=24)


def test_since_last_uses_last():
    last = NOW - timedelta(hours=30)
    assert window_start(NOW, "since_last", last, 3) == last


def test_since_last_caps_at_3_days():
    assert window_start(NOW, "since_last", NOW - timedelta(days=9), 3) == NOW - timedelta(days=3)


def test_since_last_missing_last_uses_cap():
    assert window_start(NOW, "since_last", None, 3) == NOW - timedelta(days=3)


def test_linkedin_seconds_and_indeed_days():
    f = board_filters(NOW, NOW - timedelta(hours=30))
    assert f["linkedin_f_TPR"] == "r108000"
    assert f["indeed_fromage"] == 3          # Indeed allows 1, 3, 7, 14 days
    assert f["google_tbs"] == "qdr:w"
    f1 = board_filters(NOW, NOW - timedelta(hours=24))
    assert f1["indeed_fromage"] == 1 and f1["google_tbs"] == "qdr:d"


def test_mark_success_updates_only_that_key(tmp_path):
    cfg = tmp_path / "jobscan.config.md"
    cfg.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
    before = cfg.read_text(encoding="utf-8")
    mark_success(cfg, NOW)
    after = cfg.read_text(encoding="utf-8")
    assert "last_successful_scan: '2026-12-10T09:00:00+00:00'" in after
    assert before.replace("last_successful_scan: null", "last_successful_scan: '2026-12-10T09:00:00+00:00'") == after


def test_cli_prints_json(tmp_path):
    cfg = tmp_path / "jobscan.config.md"
    cfg.write_text(TEMPLATE.read_text(encoding="utf-8").replace("window: null", "window: since_last"),
                   encoding="utf-8")
    r = subprocess.run([sys.executable, scan_window.__file__, str(cfg)], capture_output=True, text=True)
    out = json.loads(r.stdout)
    assert set(out) >= {"start", "linkedin_f_TPR", "indeed_fromage", "google_tbs"}
