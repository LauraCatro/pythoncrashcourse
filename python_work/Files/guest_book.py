from pathlib import Path

path = Path('python_work/Files/guest_book.txt')


while True:
    name = input("Introduce tu nombre y tu apellido, introduce 'salir' para terminar: ")
    if name == 'salir':
        break
    else:
        path = open('python_work/Files/guest_book.txt', mode="a",encoding="utf-8")
        path.write(name + "\n")
        path.close()

