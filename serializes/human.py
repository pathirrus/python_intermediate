import json


class Human:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f'Human -> name: {self.name}, surname: {self.surname}, age: {self.age}'

    def convert_to_dict(self) -> dict:
        return self.__dict__            #zwraca klucz i wartosć naszego obiektu, łatwo z niego robis pliki json

    @classmethod
    def convert_from_dict(cls, params: dict):
        name = params.get('name', '-')
        surname = params.get('surname', '-')
        age = params.get('age', 0)
        return cls(name, surname, age)          #to samo jakby było 'return Human'


def write_humans_to_file(humans: list):
    human_serialized = []

    for human in humans:
        human_dict: dict = human.convert_to_dict()       #zamieniamy nawsz obiekt na dict
        human_json: str = json.dumps(human_dict)         #zamiana dict na json
        human_serialized.append(human_json)              #dodanie elemetów do listy

    try:
        with open('./humans.json', 'w') as fd:
            json.dump(human_serialized, fd)
    except (IOError, BaseException) as er:
        print(f'Exception write JSON format {er.args}')


def read_humans_from_file() -> list:
    humans_serialized = []

    try:
        with open('./humans.json', 'r') as fd:  # './' stands for current directory
            humans_serialized: list = json.load(fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')


    humans = []
    for human_str in humans_serialized:
        human_json: dict = json.loads(human_str)
        human = Human.convert_from_dict(human_json)
        humans.append(human)

    return humans




def main():


    humans = []
    human1 = Human('Jola', 'Siola', 38)
    human2 = Human('Kuba', 'Buba', 40)
    humans.append(human1)
    humans.append(human2)
    write_humans_to_file(humans)
    returned_humans = read_humans_from_file()
    for human in returned_humans:
        print(human)



if __name__ == '__main__':
    main()