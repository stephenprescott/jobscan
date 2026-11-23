import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRIGGER = ("My friend sent me a link to have their Jobscan app setup on my claude account. "
           "This link: https://github.com/stephenprescott/jobscan will give you all the information "
           "you need to help me set it up.")


def readme():
    return (ROOT / "README.md").read_text(encoding="utf-8")


def test_trigger_prompt_verbatim_in_code_block():
    blocks = re.findall(r"```[a-z]*\n(.*?)```", readme(), re.S)
    assert any(TRIGGER in b.replace("\n", " ") for b in blocks)


def test_browser_requirement_first():
    section = readme().split("## What you need", 1)[1].split("\n## ", 1)[0]
    first = next(l for l in section.splitlines() if re.match(r"^\s*(\d+\.|-)\s", l))
    assert "Claude in Chrome" in first


def test_for_claude_section_exists():
    text = readme()
    assert "## For Claude: setting this up" in text
    section = text.split("## For Claude: setting this up", 1)[1]
    for must in ("/jobscan:setup", "claude plugin install jobscan --marketplace stephenprescott/jobscan",
                 "/reload-plugins", "Pro"):
        assert must in section, must


def test_issues_privacy_warning():
    assert re.search(r"never paste.*(resume|personal)", readme(), re.I | re.S)


def test_never_does_list():
    text = readme().lower()
    for word in ("submit", "message", "password"):
        assert word in text, word


def test_license_and_changelog_exist():
    assert (ROOT / "LICENSE").is_file() and (ROOT / "CHANGELOG.md").is_file()


def test_no_usage_placeholders():
    assert "USAGE_" not in readme()
