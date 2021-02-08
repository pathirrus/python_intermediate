from abc import ABC, abstractmethod


class Animals(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def drink(self):
        pass

   # @property
    def name(self) -> str:
        return self._name