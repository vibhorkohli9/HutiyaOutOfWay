import random
from datetime import datetime, timedelta
from pathlib import Path

STATE = Path(".doomsday")
MODE = Path(".mode")
README = Path("README.md")

now = datetime.utcnow()

if not STATE.exists():
    end = now + timedelta(days=random.randint(90, 180))
    STATE.write_text(end.isoformat())
    MODE.write_text("down")

end = datetime.fromisoformat(STATE.read_text())
mode = MODE.read_text().strip()

remaining = (end - now).days

if remaining <= 0 and mode == "down":
    MODE.write_text("up")

mode = MODE.read_text().strip()

if mode == "up":
    remaining = abs(remaining)

end += timedelta(days=random.choice([-1, 0, 0, 1]))
STATE.write_text(end.isoformat())

doom = f"> ☢ DOOMSDAY COUNTER: {remaining} days ({mode})"

if README.exists():
    lines = README.read_text().splitlines()
    lines = [l for l in lines if not l.startswith("> ☢ DOOMSDAY")]
    lines.insert(0, doom)
    README.write_text("\n".join(lines) + "\n")
