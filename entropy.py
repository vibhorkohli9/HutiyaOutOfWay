import random
from pathlib import Path

README = Path("README.md")

if not README.exists():
    exit(0)

lines = README.read_text().splitlines()
symbols = ["⊘", "⊘ ⊘", "⊘ ⊘ ⊘", "⊘ ⊘ ⊘ ⊘"]

meaningful = [l for l in lines if l.strip() and "⊘" not in l]

if len(meaningful) <= 2:
    README.write_text(random.choice(symbols) + "\n")
    exit(0)

victims = [i for i, l in enumerate(lines) if l.strip() and "⊘" not in l]
if victims:
    del lines[random.choice(victims)]

if random.random() < 0.4:
    lines.append(random.choice(symbols))

README.write_text("\n".join(lines) + "\n")
