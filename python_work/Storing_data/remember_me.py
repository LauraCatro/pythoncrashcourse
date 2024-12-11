from pathlib import Path
import json

usernames = input("What is your name? ")

path = Path('python_work/Storing_data/username.json')
contents = json.dumps(usernames)
path.write_text(contents)

print(f"We'll remember you when you come back {usernames}!")