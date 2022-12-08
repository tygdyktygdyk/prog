from abc import ABC, abstractmethod

class AbstractStrategy(ABC):

    @abstrctmethod
    def func(self):
        pass

class Death(AbstractStrategy):
    def func(self):
        pass

class Slowed(AbstractStrategy):
    def func(self):
        pass

class Barrier(AbstractStrategy):
    def func(self):
        pass

def situation(): # координаты объекта, определяющие место на карте
    pass
