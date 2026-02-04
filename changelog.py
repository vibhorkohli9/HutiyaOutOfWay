from datetime import datetime
from pathlib import Path

LOG = Path("CHANGELOG.md")
STATE = Path(".doomsday")
MODE = Path(".mode")

time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
end = STATE.read_text().strip() if STATE.exists() else "UNKNOWN"
mode = MODE.read_text().strip() if MODE.exists() else "?"

entry = f"""
## [{time}]
- No changes recorded.
- End state: {end}
- Direction: {mode}
"""

if not LOG.exists():
    LOG.write_text("# CHANGELOG\n\nThis file should not exist.\n")

LOG.write_text(LOG.read_text() + entry)
