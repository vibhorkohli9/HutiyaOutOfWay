from datetime import datetime
from pathlib import Path

README = Path("README.md")
MARK = Path(".last_resurrection")

now = datetime.utcnow()

if MARK.exists():
    last = datetime.fromisoformat(MARK.read_text())
    if last.year == now.year:
        exit(0)

README.write_text(
    "⊘\n\nThe system was observed.\nOne commit was permitted.\n"
)

MARK.write_text(now.isoformat())
