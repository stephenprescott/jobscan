import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for sub in ("scripts", "plugin/scripts"):
    p = str(ROOT / sub)
    if p not in sys.path:
        sys.path.insert(0, p)
