from decimal import Decimal


def exercises_1():

    names_list = ["Anna", "Bartosz", "Johan","Dolores", "Fifonż"]
    print("Case A")

    resoult_a = sorted(names_list, key=lambda name: len(name))
    print(resoult_a)

    print("Case B")
    resoult_b = sorted(names_list, key=lambda name: len(name), reverse=True)
    print(resoult_b)

    print("Case C")
    resoult_c = sorted(names_list, key=lambda name: name[0])
    print(resoult_c)



class BankAccount():
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Account name: {self.name} balance is: {self.balance}'


def exercises_2_3():
    acc_1 = BankAccount("1", Decimal(1000))
    acc_2 = BankAccount("2", Decimal(4000))
    acc_3 = BankAccount("3", Decimal(5000))
    acc_4 = BankAccount("4", Decimal(7000))
    acc_5 = BankAccount("5", Decimal(10000))

    acc_list = [acc_1, acc_2, acc_3, acc_4, acc_5]

    print("Exercises 2")

    filter_acc = list(filter(lambda acc: acc if acc.balance >Decimal(4500) else None, acc_list))
    print(filter_acc)

    max_accounts = max(acc_list, key=lambda acc: acc.balance)
    print(max_accounts)

