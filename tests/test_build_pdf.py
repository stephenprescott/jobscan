import builtins

import pytest

import build_pdf

WIN_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
WIN_EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
MAC_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MAC_EDGE = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"


def test_find_browser_windows_chrome_first():
    assert build_pdf.find_browser("win32", lambda p: p in {WIN_CHROME, WIN_EDGE}) == WIN_CHROME


def test_find_browser_windows_falls_back_to_edge():
    assert build_pdf.find_browser("win32", lambda p: p == WIN_EDGE) == WIN_EDGE


def test_find_browser_mac_chrome_then_edge():
    assert build_pdf.find_browser("darwin", lambda p: p in {MAC_CHROME, MAC_EDGE}) == MAC_CHROME
    assert build_pdf.find_browser("darwin", lambda p: p == MAC_EDGE) == MAC_EDGE


def test_find_browser_none_gives_plain_message():
    with pytest.raises(SystemExit) as e:
        build_pdf.find_browser("darwin", lambda p: False)
    assert "Install Google Chrome" in str(e.value)


def test_missing_pypdf_prints_install_hint(monkeypatch):
    real_import = builtins.__import__

    def fake_import(name, *a, **k):
        if name == "pypdf":
            raise ImportError("no pypdf")
        return real_import(name, *a, **k)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    with pytest.raises(SystemExit) as e:
        build_pdf.load_pdf_libs()
    assert "pip install pypdf pypdfium2 pillow" in str(e.value)


def test_missing_pillow_prints_install_hint(monkeypatch):
    real_import = builtins.__import__

    def fake_import(name, *a, **k):
        if name == "PIL":
            raise ImportError("no PIL")
        return real_import(name, *a, **k)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    with pytest.raises(SystemExit) as e:
        build_pdf.load_pdf_libs()
    assert "pillow" in str(e.value)


def test_max_pages_flag_default_2():
    assert build_pdf.parse_args(["a.html", "a.pdf", "pngs"]).max_pages == 2
    assert build_pdf.parse_args(["a.html", "a.pdf", "pngs", "--max-pages", "1"]).max_pages == 1
