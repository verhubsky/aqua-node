from random import random


class FishBatch(object):
    BORN_COEF = 12
    GROW_COEF = 15
    DIE_COEF = 10

    def __init__(self, species: str, count: int, avg_weight: float) -> None:
        self.__species = species
        self.__count = max(0, count)
        self.__avg_weight = max(0, avg_weight)

    def grow(self) -> None:
        self.__count += int(random() * self.BORN_COEF)
        self.__avg_weight += random() * self.GROW_COEF

    def die(self) -> None:
        self.__count = max(0, self.__count - int(random() * self.DIE_COEF))

    @property
    def species(self) -> str:
        return self.__species

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, value: int) -> None:
        self.__count = max(0, value)

    @property
    def avg_weight(self) -> float:
        return self.__avg_weight
