import subprocess

import install_hooks


def test_writes_pre_push_that_requires_denylist(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    hook = install_hooks.install(tmp_path)
    text = hook.read_text(encoding="utf-8")
    assert hook == tmp_path / ".git" / "hooks" / "pre-push"
    assert "JOBSCAN_DENYLIST" in text
    assert "privacy_scan.py . --denylist" in text
    assert "git log -p --format=%B" in text
