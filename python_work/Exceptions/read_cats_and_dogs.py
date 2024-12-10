from pathlib import Path

def contenido(path):
    """ Count the aproximate number of words in a file """
    try:
        archivo = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} doe snot exist")
    else:
        lines = archivo.splitlines()
        for line in lines:
            print(line)

filenames = ['python_work/Exceptions/dogs.txt', 
             'python_work/Exceptions/cats.txt']

print("Names of the pets")

for file in filenames:
    path = Path(file)
    contenido(path)
