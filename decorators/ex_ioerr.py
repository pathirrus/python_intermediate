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



    #
    # class PrimeIterator:
    #     # Iterator pozwalający na iterowanie po n liczbach pierwszych
    #     def __init__(self, n):
    #         self.n = n
    #         self.generated_numbers = 0
    #         self.number = 1
    #
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         self.number += 1
    #         if self.generated_numbers >= self.n:
    #             raise StopIteration
    #         elif is_prime(self.number):
    #             self.generated_numbers += 1
    #             return self.number
    #         return self.__next__()            zachodzi rekurencja 
    #
    #
    # iter = PrimeIterator(1000000)
    # for elem in iter:
    #     print(elem)