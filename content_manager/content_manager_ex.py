from contextlib import contextmanager


@contextmanager
def open_file(path: str, mode='a'):
    print("Opening file")
    fd = open(path, mode)
    yield fd
    fd.close()
    print("Closing file")


def exercise_1():
    try:
        with open_file("./text.txt") as fd:
            fd.write("Przykład ddl")
    except IOError as e:
        print(f"Found error, more info: {e.args}")
