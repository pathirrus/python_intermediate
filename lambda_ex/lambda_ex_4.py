from random import randint


def exercises_4():
    random_list = [randint(0, 101) for item in range(10)]        #lista składana
    print(f'Before: {random_list}')
    print("After")

    print(list(map(lambda number: number*2, random_list)))
