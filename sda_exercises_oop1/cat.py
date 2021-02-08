from python_intermediate.animal import Animals
from python_intermediate.movable import Movable


class Cat(Movable, Animals):

    def __init__(self, name: str, sound="miau", eaten_mouse=0):
        Animals.__init__(self, name)
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f'Name is {self.name} sound: {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Zjadłem {self.eaten_mouse} myszy')
        return self.eaten_mouse

    def move(self) -> str:
        return"idem"

    def drink(self):
        print(f'Cat drink water')