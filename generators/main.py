from python_intermediate_repo.python_intermediate.generators.exercise_3 import Iterable
from python_intermediate_repo.python_intermediate.generators.exercises_4 import generator_ex_4


def iterator_ex_1():
    dictionary = {
        'a': 1,
        'b': 5,
        'c': 7
    }

    for key in dictionary.keys():
        print(key)

    for value in dictionary.values():
        print(value)


def creator_number(n):
    list_of_num = []
    for num in range(n):
        list_of_num.append(num)
    return list_of_num


def iterator_ex_2(n):
    print("Start exercise 2")
    import sys
    result_list = creator_number(n)
    print(f'Size of list in bytes: {sys.getsizeof(result_list)}')
    result = sum(result_list)
    print((f'Size of one number in bytes: {sys.getsizeof(result)}'))
    print(result)


def iterator_ex_3(n):
    print("Start exercise 3")
    import sys
    my_iterator = Iterable(n)
    print(f'Size of iterator in bytes: {sys.getsizeof(my_iterator)}')
    result = sum(my_iterator)
    print((f'Size of one number in bytes: {sys.getsizeof(result)}'))
    print(result)


def main():
    # # iterator_ex_1()
    # print("Exercise 2")
    # iterator_ex_2(100000)
    # print("Exercise 3")
    # iterator_ex_3(100000)
    generator_ex_4()

if __name__ == "__main__":
    main()
