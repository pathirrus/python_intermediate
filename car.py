from sda_exercises_oop_1.movable import Movable


class Car(Movable):

   # def __init__(self):       jeśli nie jest to napisane to python sam to przy interpretacji dodaje
   #     pass

    def move(self):
        return ("jadę")