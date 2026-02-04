import os
import requests
from datetime import datetime
from pathlib import Path

STATE = Path(".doomsday")
REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["ARCHIVE_TOKEN"]

end = datetime.fromisoformat(STATE.read_text())
remaining = (end - datetime.utcnow()).days

if remaining > -30:
    exit(0)

url = f"https://api.github.com/repos/{REPO}"
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

requests.patch(url, headers=headers, json={"archived": True})
