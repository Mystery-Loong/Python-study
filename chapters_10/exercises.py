# 10.1
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines().lstrip()
for line in lines: