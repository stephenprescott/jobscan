"""Privacy scan tests. Sensitive-looking strings are built at runtime so this
file itself never trips the scan."""
import subprocess
import sys
from pathlib import Path

import privacy_scan
from privacy_scan import scan

SCRIPT = Path(privacy_scan.__file__)
PHONE = "555" + "-123-" + "4567"
ARTIFACT = "claude.ai/" + "artifact/AbC123"


def write(tmp_path, name, text):
    p = tmp_path / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def test_flags_denylisted_term_case_insensitive(tmp_path):
    write(tmp_path, "a.md", "line one\nworked at acme corp\n")
    found = scan(tmp_path, ["Acme Corp"])
    assert [(f.path, f.line, f.term) for f in found] == [("a.md", 2, "Acme Corp")]


def test_flags_us_phone_pattern(tmp_path):
    write(tmp_path, "a.md", f"call {PHONE}\n")
    found = scan(tmp_path, [])
    assert len(found) == 1 and found[0].term == "phone number"


def test_flags_claude_artifact_url(tmp_path):
    write(tmp_path, "a.md", f"board: https://{ARTIFACT}\n")
    found = scan(tmp_path, [])
    assert len(found) == 1 and found[0].term == "claude artifact link"


def test_flags_real_email(tmp_path):
    write(tmp_path, "a.md", "mail " + "jane.doe" + "@" + "gmail.com\n")
    assert scan(tmp_path, [])[0].term == "email address"


def test_ignores_git_dir_and_binary_files(tmp_path):
    write(tmp_path, ".git/config", "acme corp\n")
    (tmp_path / "img.png").write_bytes(b"\x89PNG\x00\x00acme corp")
    assert scan(tmp_path, ["acme corp"]) == []


def test_allows_placeholders(tmp_path):
    write(tmp_path, "a.md", "Phone: [your phone]\nEmail: you@example.com\n")
    assert scan(tmp_path, []) == []


def test_denylist_file_skips_blanks_and_comments(tmp_path):
    dl = write(tmp_path / "x", "deny.txt", "# comment\n\nAcme\n")
    assert privacy_scan.load_denylist(dl) == ["Acme"]


def test_cli_exit_codes(tmp_path):
    repo = tmp_path / "repo"
    write(repo, "a.md", "clean text\n")
    dl = write(tmp_path, "deny.txt", "acme\n")
    run = lambda: subprocess.run([sys.executable, str(SCRIPT), str(repo), "--denylist", str(dl)],
                                 capture_output=True, text=True)
    assert run().returncode == 0
    write(repo, "b.md", "ACME\n")
    r = run()
    assert r.returncode == 1 and "b.md:1" in r.stdout


def test_ignores_decorators_in_diff_lines():
    assert privacy_scan.scan_text("+" + "@pytest.mark.skipif(x)\n", "d", []) == []


def test_allows_public_noreply_addresses():
    text = "Co-Authored-By: Claude <noreply" + "@anthropic.com>\n" \
           "Author: me <1+me" + "@users.noreply.github.com>\n"
    assert privacy_scan.scan_text(text, "log", []) == []
