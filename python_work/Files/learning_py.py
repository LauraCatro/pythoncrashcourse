from pathlib import Path

path = Path('python_work/Files/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


print(contents)
print(lines)
