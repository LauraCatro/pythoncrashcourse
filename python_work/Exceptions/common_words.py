from pathlib import Path

path = Path('python_work/Exceptions/moby_dick.txt')

contents = path.read_text(encoding='utf-8')
time = contents.count('the ')
print(time)
