from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(type(contents))
print(type(numbers))
print(numbers)