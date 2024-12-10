from pathlib import Path

path = Path('python_work/Files/guest_book.txt')


while True:
    name = input("Enter your firts name and last name, enter 'exit' to quit: ")
    if name == 'exit':
        break
    else:
        path = open('python_work/Files/guest_book.txt', mode="a",encoding="utf-8")
        path.write(name + "\n")
        path.close()

