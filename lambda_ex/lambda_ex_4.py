from random import randint


def exercises_4():
    random_list = [randint(0, 101) for item in range(10)]        #lista składana
    print(f'Before: {random_list}')
    print(f"After and {type(random_list)}")

    print(list(map(lambda number: number*2, random_list)))
def exercises_5():
    rand_list = [randint(100, 200) for item in range(20)]
    print(f'Random list:\n{rand_list}')
    print(f'Sorted min to max:\n{sorted(rand_list)} ')
    print(f'Sorted max to min:\n{sorted(rand_list, reverse=True)} ')
