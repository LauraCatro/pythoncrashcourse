from pathlib import Path

def count_words(path):
    """ Count the aproximate number of words in a file """
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doe snot exist")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        number_words = len(words)
        print(f"The file {path} has about {number_words} words")


filenames = ['python_work/Exceptions/alice.txt', 
             'python_work/Exceptions/siddhartha.txt',
             'python_work/Exceptions/littlea_woman.txt',
             'python_work/Exceptions/moby_dick.txt']
for filename in filenames:
    print("\n")
    path = Path(filename)
    print(type(filename))
    print(type(path))
    count_words(path)

