def main():
    a, b = print_hello(1, 2)
    print(f'In main {a, b}')


def wrap_before_and_after(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@wrap_before_and_after
def print_hello(a, b):
    print("Hello world! :)")
    print(f'{a, b}')
    print("ddsd")
    x = 2+2
    print(x)
    return a, b


if __name__ == '__main__':
    main()
