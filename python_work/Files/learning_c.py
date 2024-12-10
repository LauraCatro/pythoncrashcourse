from pathlib import Path

path = Path('python_work/Files/learning_python.txt')
contents = path.read_text().replace('Python', 'C')

print(contents)
