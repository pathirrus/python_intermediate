import re


def exercises_1():
    print("Write number here:")
    value = input()

    expression = "[0-9]+"
    if re.fullmatch(expression, value):
        print("Found number")
        if int(value) %2==0:
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
    expression = "[\w]{8,16}"
    if re.fullmatch(expression, check_login):
        print("Login is correct")


    else:
        print(("Login is NOT correct"))



