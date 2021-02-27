import re


def exercises_1():
    print("Write number here:")
    value = input()

    expression = "[0-9]+"
    if re.fullmatch(expression, value):
        print("Found number")
        if int(value) % 2 == 0:
            print("Number is even")
        else:
            print("Number is not even")
    else:
        print(("Incorrect input"))


def exercises_2():
    print("Write post code here:")
    value = input()

    expression = "[0-9]{2}-[0-9]{3}"
    if re.fullmatch(expression, value):
        print("Correct post code")


    else:
        print(("Incorrect post code"))


def exercises_3():
    print("Write your login:")
    check_login = input()
    expression = "[\w_]{8,16}"
    if re.fullmatch(expression, check_login):
        print("Login is correct")


    else:
        print(("Login is NOT correct"))


def exercises_4():
    print("enter any string of characters:")
    value = input()

    expression = ".*ala.*"
    if re.match(expression, value):
        print("found ala")
    else:
        print("ala not found")


def exercises_7():
    print("Enter serial number:")
    value = input()

    expression = r'([A-Z0-9!@#\$%\^&\*]{5}-){4}[A-Z0-9!@#\$%\^&\*]{5}'
    if re.fullmatch(expression, value):
        print("Serial number is correct")
    else:
        print("Serial number is incorretct")


def exercises_9():
    text = "Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę\
stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy\
rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków\
aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie\
struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś\
teorię, okazuje się jasne."

    empty_string = ""
    words_number = text.split()
    print(f'Words number: {len(words_number)}')

    char_number = re.split(empty_string, text)
    print(f'Char number: {char_number}')

    average_operation = [len(char_number) for char_number in words_number]
    # print(average_operation)
    average = sum(average_operation)/len(average_operation)
    print(f'The average word length is: {average:.2f}')

    max_word = [len(char_number) for char_number in words_number]
    print(f'The longest number of characters in a word: {max(max_word)}')

    min_word = [len(char_number) for char_number in words_number]
    print(f'The shortest number of characters in a word: {min(min_word)}')