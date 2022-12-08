from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def creature_unit_c(self) -> AbstractUnitC:
        pass

class ConcreteFactory1(AbstractFactory):

    def creature_unit_a(self) -> AbstractUnitA:
        return ConcreteUnitA1()
    def creature_unit_b(self) -> AbstractUnitB:
        return ConcreteUnitB1()
    def creature_unit_c(self) -> AbstractUnitC:
        return ConcreteUnitC1()

class ConcreteFactory2(AbstractFactory):

    def creature_unit_a(self) -> AbstractUnitA:
        return ConcreteUnitA2()
    def creature_unit_b(self) -> AbstractUnitB:
        return ConcreteUnitB2()
    def creature_unit_c(self) -> AbstractUnitC:
        return ConcreteUnitC2()

#растения
class AbstractUnitA(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def get_coords(self):
        pass

    @abstractmethod
    def set_coords(self, x, y):
        pass

    @abstractmethod
    def get_emoji(self):
        pass

#кактус
class ConcreteUnitA1(AbstractUnitA):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001F335'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji

#мухомор
class ConcreteUnitA2(AbstractUnitA):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001F344'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji
#насекомые
class AbstractUnitB(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def get_coords(self):
        pass

    @abstractmethod
    def set_coords(self, x, y):
        pass

    @abstractmethod
    def get_emoji(self):
        pass

#таракан
class ConcreteUnitB1(AbstractUnitB):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001FAB3'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji

#муха
class ConcreteUnitB2(AbstractUnitB):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001FAB0'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji
#люди
class AbstractUnitC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def get_coords(self):
        pass

    @abstractmethod
    def set_coords(self, x, y):
        pass

    @abstractmethod
    def get_emoji(self):
        pass

#фехтовальщик
class ConcreteUnitC1(AbstractUnitC):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001F93A'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji

#гольфист
class ConcreteUnitC2(AbstractUnitC):
    def __init__(self):
        self.__x = 6; self.__y = 6; self.__health = 10
        self.__armor = 10; self.__atack = 10; self.__emoji = '\U0001F3CC'

    def move(self, direction):
        if direction == 'w': self.__y -= 1
        elif direction == 'd': self.__x += 1
        elif direction == 's': self.__y += 1
        elif direction == 'a': self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_emoji(self):
        return self.__emoji

def create_unit(factory: AbstractFactory, space: Space, units, typ, x, y):
    if typ == 'A':
        unit = factory.creature_unit_a()
    elif typ == 'B':
        unit = factory.creature_unit_b()
    elif typ == 'C':
        unit = factory.creature_unit_c()
    unit.set_coords(x, y)
    space.enter_object(unit.get_coords(), unit.get_emoji())
    units.append(unit)
