from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_unit_a(self)->AbstractUnitA:
        pass

    @abstractmethod
    def create_unit_b(self)->AbstractUnitB:
        pass

    @abstractmethod
    def create_unit_c(self)->AbstractUnitC:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_unit_a(self)->AbstractUnitA:
        return ConcreteUnitA1()

    def create_unit_b(self)->AbstractUnitB:
        return ConcreteUnitB1()

    def create_unit_c(self)->AbstractUnitC:
        return ConcreteUnitC1()

class ConcreteFactory2(AbstractFactory):
    def create_unit_a(self)->AbstractUnitA:
        return ConcreteUnitA2()

    def create_unit_b(self)->AbstractUnitB:
        return ConcreteUnitB2()

    def create_unit_c(self)->AbstractUnitC:
        return ConcreteUnitC2()

class AbstractUnitA(ABC):
    @abstractmethod
    def __init__(self):
        pass

class ConcreteUnitA1(AbstractUnitA):
    def __init__(self):
        self.x = 6;
        self.y = 10;

class ConcreteUnitA2(AbstractUnitA):
    def func_a(self, x):
        return "The result of the unit A2."

class AbstractUnitB(ABC):
    @abstractmethod
    def func_b(self):
        pass

class ConcreteUnitB1(AbstractUnitB):
    def func_b(self):
        return "The result of the unit B1."

class ConcreteUnitB2(AbstractUnitB):
    def func_b(self):
        return "The result of the unit B2."

class AbstractUnitC(ABC):
    @abstractmethod
    def func_c(self):
        pass

class ConcreteUnitC1(AbstractUnitC):
    def func_c(self):
        return "The result of the unit C1."

class ConcreteUnitC2(AbstractUnitC):
    def func_c(self):
        return "The result of the unit C2."

def client_code(factory: AbstractFactory, x, y)->None:

    unit_a = factory.create_unit_a()
    return unit_a
    
unit = client_code(ConcreteFactory1(), 6, 10)
print(unit.x, unit.y)

