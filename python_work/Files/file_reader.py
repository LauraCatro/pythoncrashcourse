from pathlib import Path

path = Path('python_work/Files/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)

# lines = contents.splitlines()

# for line in lines:
#     print(line)