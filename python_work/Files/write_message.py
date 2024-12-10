from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new game.\n"
contents += "I also love working with data.\n"

path = Path('python_work/Files/programming.txt')
path.write_text(contents)