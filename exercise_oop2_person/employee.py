from datetime import date
from python_intermediate_repo.python_intermediate.exercise_oop2_person.person import Person


class Employee(Person):

    def __init__(self, name: str, surname: str, birth_date: date, salary=1000.0):
        birth_date = self.check_birth_date(birth_date)
        super().__init__(name, surname, birth_date)
        self._salary = salary

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        value = self.check_birth_date(value)
        self.birth_date = value

    @staticmethod
    def check_birth_date(value: date) -> date:
        if value > date.today() or \
                value < date(year=1920, month=12, day=31):
            value = date(0, 0, 0)
        return value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value

    def who_am_i(self):
        print(f'I am {self.name} {self.surname} and I earn: {self.salary} $')
