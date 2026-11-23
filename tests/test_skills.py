"""Static checks on the plugin's skills: front matter, plugin-relative paths,
reads from the friend's data folder, and no personal leftovers."""
import os
import re
from pathlib import Path

import pytest
import yaml

from privacy_scan import load_denylist, scan_text

SKILLS = Path(__file__).resolve().parent.parent / "plugin" / "skills"


def skill(name):
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


def front(name):
    m = re.match(r"^---\n(.*?)\n---\n", skill(name), re.S)
    assert m, f"{name}: no front matter"
    return yaml.safe_load(m.group(1))


EXPECT = {
    "setup": ["setup-progress.md", "references/preflight.md", "references/honest-resume.md",
              "references/questions.md", "references/finish.md", "${CLAUDE_PLUGIN_ROOT}/templates",
              "AskUserQuestion", "continue jobscan setup", "(Recommended)", "Other",
              "In the reference files"],
    "apply": ["apply_outputs", "hm_search", "form_fill", "Ask me each time", "voice-rules.md",
              "applications/profile.md", "applications/postings/", "tracker.md", "/jobscan:tailor-resume",
              "`light`", "Stop before submit", "settings", "/jobscan:apply 2026-12-01 #2"],
    "jobscan": ["applications/criteria.md", "seen.csv", "tracker.md", "references/sources.md",
                "${CLAUDE_PLUGIN_ROOT}/scripts/scan_window.py", "--mark-success", "blocked:",
                "stopped: usage limit", "`notify`", "skip it if unavailable", "match unverified", "years in that same area", "`board_url`", "`mode`", "`sources`", "settings"],
    "tailor-resume": ["resume_doc_url", "resume_max_pages", "confirmed-facts.md", "voice-rules.md",
                      "${CLAUDE_PLUGIN_ROOT}/scripts/build_pdf.py", "resumes/_template.html"],
}


@pytest.mark.parametrize("name", sorted(EXPECT))
def test_front_matter(name):
    fm = front(name)
    assert fm["name"] == name
    assert len(fm["description"]) > 80


@pytest.mark.parametrize("name", sorted(EXPECT))
def test_reads_from_data_folder(name):
    text = skill(name)
    missing = [t for t in EXPECT[name] if t not in text]
    assert missing == []


@pytest.mark.parametrize("name", sorted(EXPECT))
def test_no_personal_leftovers(name):
    text = skill(name)
    for t in ("Stephen", "Job Search HQ", "Resume session", "Kanzo"):
        assert t not in text, t


@pytest.mark.parametrize("name", sorted(EXPECT))
def test_no_windows_only_paths(name):
    assert "C:\\" not in skill(name)


@pytest.mark.skipif(not os.environ.get("JOBSCAN_DENYLIST"), reason="JOBSCAN_DENYLIST not set")
@pytest.mark.parametrize("name", sorted(EXPECT))
def test_privacy(name):
    assert scan_text(skill(name), name, load_denylist(os.environ["JOBSCAN_DENYLIST"])) == []
