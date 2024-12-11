from pathlib import Path
import json

path = Path('python_work/Storing_data/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(f"\nNumbers: {numbers}")
