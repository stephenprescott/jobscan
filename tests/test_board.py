import os
import re
from pathlib import Path

import pytest

from privacy_scan import load_denylist, scan_text

BOARD = Path(__file__).resolve().parent.parent / "plugin" / "board" / "jobscan-board.html"


def html():
    return BOARD.read_text(encoding="utf-8")


def test_no_hardcoded_fit_thresholds():
    h = html()
    assert ">= 7" not in h and ">= 3" not in h
    assert "Want 7+" not in h


def test_reads_settings_board_doc():
    h = html()
    assert 'collection("settings")' in h
    for key in ("fit_want", "fit_match", "want_max", "title"):
        assert key in h, key


def test_fit_chip_hidden_until_settings():
    assert re.search(r'id="fit-group"[^>]*hidden', html())


def test_apply_comment_format():
    assert '"/jobscan:apply " + j.date + " #" + j.num' in html()


def test_unverified_match_jobs_always_shown():
    assert '"match unverified"' in html()


def test_no_personal_strings():
    h = html()
    assert "Stephen" not in h and "Job Search HQ" not in h
    assert "9am, 12pm and 7pm" not in h


@pytest.mark.skipif(not os.environ.get("JOBSCAN_DENYLIST"), reason="JOBSCAN_DENYLIST not set")
def test_board_passes_privacy_scan():
    assert scan_text(html(), "board", load_denylist(os.environ["JOBSCAN_DENYLIST"])) == []
