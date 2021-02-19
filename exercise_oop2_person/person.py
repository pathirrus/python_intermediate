from datetime import date


class Person:
    def __init__(self, name: str, surname: str, birth_date: date):
        self._name = name
        self._surname = surname
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value: str):
        self._surname = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        self._birth_date = value
