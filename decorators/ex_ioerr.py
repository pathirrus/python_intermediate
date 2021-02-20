def catch_io_error_decorator(func):
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


def main():
    throw_exception_file()


if __name__ == "__main__":
    main()
