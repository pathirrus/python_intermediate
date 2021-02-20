from six import wraps


def catch_io_error_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IOError as e:
            print(f'IOerror cought: {e.args}')
            return None

    return inner


def catch_io_error_with_wraps(func):

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IOError as e:
            print(f'IOerror cought: {e.args}')
            return None

    return inner

@catch_io_error_decorator
def throw_exception_file():
    raise IOError('Test error')

@catch_io_error_with_wraps
def read_does_not_exist_file():
    with open("./training.notexist", 'r') as fd:
        fd.read()

def main():
    # throw_exception_file()
    read_does_not_exist_file()

if __name__ == "__main__":
    main()
