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


def main():
    # iterator_ex_1()
    iterator_ex_2(100000)

if __name__ == "__main__":
    main()
