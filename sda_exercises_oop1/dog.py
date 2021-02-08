from python_intermediate.animal import Animals


class Dog(Animals):
    def drink(self):
        print("Dog dring beer")

    def __init__(self, name: str, sound="hau"):
        super().__init__(name)          #wykorzysstujemy super bo ma tylko jeden arg
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog name is {self.name} sound: {self.sound}'