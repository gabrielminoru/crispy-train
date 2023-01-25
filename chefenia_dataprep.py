from pathlib import Path

path = Path("data") / "chefenia.txt"

text = path.read_text()

new = []
for t in text.split('\n\n'):
    new.append(t.replace('\n', ' '))

Path("data/chefenia_processed.txt").write_text('\n'.join(new))