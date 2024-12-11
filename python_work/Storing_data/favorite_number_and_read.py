from pathlib import Path
import json

path = Path('python_work/Storing_data/favorite_number.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number}")
else:
    favorite_number = input("What's your favorite number? ")
    number = json.dumps(favorite_number)
    path.write_text(number)
