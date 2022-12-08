import random
import units
class Base:
    def __init__(self, x, y):
        self.__x = x; self.__y = y; self.__health = 50; self.__count = 16
        self.__max_number_of_units = 5; self.__emoji = '\U0001F6D6'

    def get_emoji(self):
        return self.__emoji

    def set_coords(self, x, y):
        return self.__x; self.__y

    def get_coords(self):
        return self.__x, self.__y

    def add_new_unit(self, factory, space, units_list, x, y):
        if self.__count != 0:
            self.__count -= 1
            unit = units.create_unit(factory, space, units_list, 'A', x, y)

def add_new_base(space, x, y):
    base = Base(x, y)
    space.enter_object([x, y], base.get_emoji())
    return base

def trigger(space, units_list, base):
    enemy = units_list[0]
    coords1 = list(enemy.get_coords())
    coords2 = list(base.get_coords())
    if abs(coords1[0] - coords2[0]) <= 1 or abs(coords1[1] - coords2[1]) <= 1:
        base.add_new_unit(units.ConcreteFactory1(), space, units_list, random.randint(1, 11), random.randint(1, 11))
        base.add_new_unit(units.ConcreteFactory2(), space, units_list, random.randint(1, 11), random.randint(1, 11))
