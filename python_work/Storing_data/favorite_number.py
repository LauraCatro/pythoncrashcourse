from pathlib import Path
import json

favorite_number = input("What's your favorite number? ")

path = Path('python_work/Storing_data/favorite_number.json')
number = json.dumps(favorite_number)
path.write_text(number)
