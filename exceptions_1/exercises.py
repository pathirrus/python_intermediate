import sys


def case_1():
    list_of_numbers = [1, 2, 31, 54, 32]

    print("Case_1 before")
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'1. Exceptions caught {ie.args}')
    except Exception as ex:
        print(f'2. Exception cought{ex.args}')
    print("Case_1 after")

    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'3. Exceptions caught {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty')
    print(f'Given name is {name}')


def case_3(nemerator: int, denumerator: int) -> float:
    resoult = 0
    try:
        resoult = nemerator / denumerator
    except ZeroDivisionError as zde:
        print("Nie dziel przez 0!")
        # resoult = sys.float_info.max
        resoult = float(sys.maxsize)
    return resoult


def case_4(dictionary: dict):
    key = 'items'
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as ke:
        print(f'Key {key} not found, more info {ke.args}')


def case_4_v2(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if not items:
        print('Empty list or key dont exist')


def case_6():
    raise NotImplementedError('Solved in future')


def case_7():
    fd = None
    try:
        fd = open('C:/Users/Patryq/Desktop/aaa.txt')
    except IOError as ioer:
        print(f'Exception cought {ioer.args}')
    finally:
        if fd:
            print('File descriptor closing')
            fd.close()


def case_7_v2():
    try:
        with open('C:/Users/Patryq/Desktop/aaa.txt') as fd:
            print('File is open')
    except IOError as ioer:
        print(f'Exception cought {ioer.args}')
