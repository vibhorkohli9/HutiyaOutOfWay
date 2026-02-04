from datetime import datetime
from pathlib import Path

README = Path("README.md")
MARK = Path(".last_resurrection")

now = datetime.utcnow()

# Only once per year
if MARK.exists():
    last = datetime.fromisoformat(MARK.read_text())
    if last.year == now.year:
        exit(0)

# Resurrection text
text = """
⊘

The system was observed.
One commit was permitted.
Normal decay will resume.
"""

README.write_text(text.strip() + "\n")
MARK.write_text(now.isoformat())
