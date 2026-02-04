from datetime import datetime
from pathlib import Path

log_file = Path("CHANGELOG.md")

time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
log_text = f"## [{time}]\n- Chaos ticked.\n\n"

# Append to the file
log_file.open("a").write(log_text)
