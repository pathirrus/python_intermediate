from python_intermediate_repo.python_intermediate.exercise_oop2_person.employee import Employee
from datetime import date

def main():
    employee1 = Employee('Fred', 'Stonefil', date(1960, 11, 12), 5512.36)
    employee2 = Employee('Miecio', 'Kalosz', date(1909, 1, 25), 8582.32)
    print(employee1.salary, employee2.birth_date)

    employee1.who_am_i()
    employee2.who_am_i()

if __name__ == '__main__':
    main()