import datetime


class Person:
    def __init__(self, name: str, surname: str, birth_date: datetime.date):
        self._name = name
        self._surname = surname
        self._birth_date = birth_date
