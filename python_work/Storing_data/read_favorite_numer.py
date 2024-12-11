from pathlib import Path
import json

path = Path('python_work/Storing_data/favorite_number.json')
contents = path.read_text()
favorite_number = json.loads(contents)

print(f"I know your favorite number! It's {favorite_number}")
