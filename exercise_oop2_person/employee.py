from datetime import date
from python_intermediate_repo.python_intermediate.exercise_oop2_person.person import Person


class Employee(Person):

    @staticmethod
    def check_birth_date(value: date) -> date:
        if value > date.today() or \
                value < date(year=1920, month=12, day=31):
            value = date(0, 0, 0)
        return value

