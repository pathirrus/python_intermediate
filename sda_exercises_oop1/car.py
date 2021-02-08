from python_intermediate.movable import Movable


class Car(Movable):

   # def __init__(self):       jeśli nie jest to napisane to python sam to przy interpretacji dodaje
   #     pass

    def move(self):
        return ("jadę")