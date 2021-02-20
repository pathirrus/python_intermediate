def check_file_wrapper(func):
    def inner(*args, **kwargs):
        path = ''
        if len(args) > 0:
            print(f'Found args {args}')
            path = args[0]
        elif kwargs.get('file_path', ''):
            print(f'Found kwargs file path = {kwargs.get("file_path")}')
            path = kwargs.get('file_path')
        import os
        if path and os.path.exists(path):
            print('Path exist')
        elif path:
            print('File not exist, it will be created')
            from pathlib import Path
            Path(path).touch()
        else:
            print('Ther are no arguments')
            import sys
            sys.exit(1)
        return func(*args, **kwargs)

    return inner


@check_file_wrapper
def read_file(file_path: str):
    with open(file_path, 'r') as fd:  # metoda czytania z pliku
        fd.read()
