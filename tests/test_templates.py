import os
import re
from pathlib import Path

import pytest
import yaml

from privacy_scan import load_denylist, scan

T = Path(__file__).resolve().parent.parent / "plugin" / "templates"

FILES = [
    "CLAUDE.md", "jobscan.config.md", "setup-progress.md",
    "applications/criteria.md", "applications/profile.md", "applications/tracker.md",
    "applications/jobscan/seen.csv", "confirmed-facts.md", "voice-rules.md",
    "resumes/_template.html", "cover-letters/_template.html",
]

CONFIG_KEYS = {
    "data_folder", "resume_doc_url", "board_url", "state", "home_zip", "max_commute_minutes",
    "mode", "sources", "window", "window_cap_days", "last_successful_scan",
    "scan_times", "notify", "fit_bar", "apply_outputs", "hm_search", "form_fill",
    "resume_max_pages", "auto_update",
}

SOURCE_IDS = ["linkedin", "indeed", "google_jobs", "hiring_systems", "builtin",
              "wellfound", "dice", "state_site", "usajobs", "target_companies"]


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "missing YAML front matter"
    return yaml.safe_load(m.group(1))


def test_all_template_files_exist():
    missing = [f for f in FILES if not (T / f).is_file()]
    assert missing == []


def test_config_front_matter_has_exact_keys():
    cfg = front_matter(T / "jobscan.config.md")
    assert set(cfg) == CONFIG_KEYS
    assert cfg["window_cap_days"] == 3
    assert set(cfg["fit_bar"]) == {"want", "match"}
    assert set(cfg["apply_outputs"]) == {"A", "B", "C"} == set(cfg["hm_search"])


def test_config_documents_every_source_id():
    text = (T / "jobscan.config.md").read_text(encoding="utf-8")
    assert all(s in text for s in SOURCE_IDS)


def test_config_personal_values_blank():
    cfg = front_matter(T / "jobscan.config.md")
    for k in ("state", "home_zip", "max_commute_minutes", "mode", "window", "last_successful_scan"):
        assert cfg[k] is None, k
    assert cfg["sources"] == [] and cfg["scan_times"] == []


def test_criteria_has_section_headings():
    text = (T / "applications/criteria.md").read_text(encoding="utf-8")
    for h in ["## 1. Filters", "## 2. Want score", "## 3. Match score", "## 4. Tiers",
              "## Titles to search", "## Sources", "## Target companies"]:
        assert h in text, h


def test_no_values_prefilled():
    for f in ("applications/criteria.md", "applications/profile.md"):
        text = (T / f).read_text(encoding="utf-8")
        assert not re.search(r"\$\s?\d", text), f
        assert not re.search(r"\b\d{5}\b", text), f


def test_years_filter_is_relative_and_by_area():
    text = (T / "applications/criteria.md").read_text(encoding="utf-8")
    assert "more years than I have" in text
    assert "in the specific area the posting names" in text


def test_profile_has_ask_each_time_list():
    assert "## Ask me each time" in (T / "applications/profile.md").read_text(encoding="utf-8")


def test_voice_rules_one_rule_per_line():
    lines = [l for l in (T / "voice-rules.md").read_text(encoding="utf-8").splitlines()
             if l.startswith("- ")]
    assert len(lines) >= 8
    assert any("em dash" in l for l in lines)
    assert "Sign-off: [ ]" in (T / "voice-rules.md").read_text(encoding="utf-8")


def test_setup_progress_lists_ten_phases():
    text = (T / "setup-progress.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^- \[ \] Phase \d+", text, re.M)) == 10
    assert "## Answers" in text


def test_seen_csv_header():
    assert (T / "applications/jobscan/seen.csv").read_text(encoding="utf-8").strip() == \
        "key,company,title,location,first_seen,apply_url"


@pytest.mark.skipif(not os.environ.get("JOBSCAN_DENYLIST"), reason="JOBSCAN_DENYLIST not set")
def test_templates_pass_privacy_scan():
    assert scan(T, load_denylist(os.environ["JOBSCAN_DENYLIST"])) == []
