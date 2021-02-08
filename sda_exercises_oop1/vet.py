from python_intermediate.animal import Animals
from python_intermediate.cat import Cat
from python_intermediate.dog import Dog


class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat) -> str:
        return f"Witaj {cat.name}"

    @staticmethod
    def say_dog_hello(dog: Dog):
        print(f"Siemanko {dog.name}")

    #@staticmethod
    def say_animal_hi(self, animal: Animals):
        print(f"Dzień dobry {animal.name}!")