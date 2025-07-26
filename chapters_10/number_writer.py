from pathlib import Path
import json

numbers = [1,3,5,7,9,11,24]

path = Path('numbers.json')
contents = json.dumps(numbers)
print(type(contents))
path.write_text(contents)