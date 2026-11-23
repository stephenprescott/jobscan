"""Every personal decision (design 6.5) has a question in setup, and every
config key a friend chooses is written by some question."""
import re
from pathlib import Path

import pytest

REF = Path(__file__).resolve().parent.parent / "plugin" / "skills" / "setup" / "references"

DECISIONS = [
    # install
    "data_folder_location", "auto_update",
    # resume
    "resume_source", "resume_sections", "resume_max_pages", "contact_details",
    # direction
    "current_situation", "target_roles", "step_level", "move_away_from", "industries",
    # job rules
    "titles_main", "titles_stretch", "role_filter", "pay_target", "pay_floor", "pay_not_posted",
    "hourly_gigs", "work_setup", "home_zip", "max_commute", "remote_states", "employment_types",
    "contract_to_hire_rate", "max_travel", "levels_to_drop", "max_years", "clearance", "recruiters",
    "want_categories", "want_weights", "years_experience", "close_equivalents", "tier_thresholds",
    "fit_bar", "target_companies",
    # scan
    "mode", "sources", "state_site", "window", "window_cap_days", "scan_times", "notify",
    # apply
    "apply_outputs", "hm_search", "form_fill", "salary_entry", "ask_each_time",
    # profile
    "contact", "work_authorization", "sponsorship", "start_date", "relocation",
    "travel_willingness", "screening", "eeo",
    # writing
    "voice_rules", "own_rules", "sign_off",
    # board
    "publish_board", "pin_board",
]

CONFIG_KEYS_ASKED = ["state", "home_zip", "max_commute_minutes", "mode", "sources", "window",
                     "window_cap_days", "scan_times", "notify", "fit_bar", "apply_outputs",
                     "hm_search", "form_fill", "resume_max_pages", "auto_update"]


def questions():
    text = (REF / "questions.md").read_text(encoding="utf-8")
    blocks = re.split(r"^### ", text, flags=re.M)[1:]
    return {b.split("\n", 1)[0].strip(): b for b in blocks}


def test_every_decision_has_a_question():
    missing = [d for d in DECISIONS if d not in questions()]
    assert missing == []


@pytest.mark.parametrize("key", CONFIG_KEYS_ASKED)
def test_every_config_key_is_written(key):
    writers = [q for q, b in questions().items() if re.search(rf"jobscan\.config\.md: `?{key}`?\b", b)]
    assert writers, key


def test_every_question_has_choices_recommendation_and_target():
    bad = [q for q, b in questions().items()
           if not all(f"- {k}:" in b for k in ("Asks", "Choices", "Recommended", "Writes"))]
    assert bad == []
