"""Print an HTML resume or letter to PDF with headless Chrome (or Edge), report
the page count, and render each page to PNG so the layout can be checked.

Usage: python -I build_pdf.py <input.html> <output.pdf> <png_dir> [--max-pages N]
Needs: Google Chrome or Microsoft Edge, and `pip install pypdf pypdfium2 pillow`.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

BROWSERS = {
    "win32": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ],
    "darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ],
}


def find_browser(platform: str = sys.platform, exists=lambda p: Path(p).exists()) -> str:
    for p in BROWSERS.get(platform, []):
        if exists(p):
            return p
    sys.exit("No Chrome or Edge found. Install Google Chrome (https://www.google.com/chrome/) and try again.")


def load_pdf_libs():
    try:
        from pypdf import PdfReader
        import pypdfium2
        import PIL  # noqa: F401  (pypdfium2 renders page images through Pillow)
    except ImportError:
        sys.exit("Missing PDF tools. Run: python -m pip install pypdf pypdfium2 pillow")
    return PdfReader, pypdfium2


def parse_args(argv):
    ap = argparse.ArgumentParser(description="Build a PDF from HTML and check its pages.")
    ap.add_argument("html")
    ap.add_argument("pdf")
    ap.add_argument("png_dir")
    ap.add_argument("--max-pages", type=int, default=2)
    return ap.parse_args(argv)


def main(argv=None) -> None:
    a = parse_args(sys.argv[1:] if argv is None else argv)
    html, pdf, png_dir = (Path(x).resolve() for x in (a.html, a.pdf, a.png_dir))
    PdfReader, pypdfium2 = load_pdf_libs()
    png_dir.mkdir(parents=True, exist_ok=True)
    pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [find_browser(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--user-data-dir={profile}", f"--print-to-pdf={pdf}", html.as_uri()],
            check=True, capture_output=True,
        )
    pages = len(PdfReader(str(pdf)).pages)
    doc = pypdfium2.PdfDocument(str(pdf))
    pngs = []
    for i in range(len(doc)):
        out = png_dir / f"page{i + 1}.png"
        doc[i].render(scale=1.3).to_pil().save(out)
        pngs.append(str(out))
    doc.close()
    print(f"PDF: {pdf}")
    over = f"  <-- over {a.max_pages} pages, tighten content" if pages > a.max_pages else ""
    print(f"Pages: {pages}{over}")
    print("Page images:", *pngs, sep="\n  ")


if __name__ == "__main__":
    main()
