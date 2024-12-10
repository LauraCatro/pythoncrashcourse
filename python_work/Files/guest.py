from pathlib import Path

path = Path('python_work/Files/guest.txt')
name = input("Please enter your name: ")

path.write_text(name)



 