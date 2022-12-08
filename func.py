import random
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def action(self, gspace, landscape, unit, coords):
        pass

class Move(Strategy):
    def action(self, space, landscape, unit, coords):
        space.delete_object(unit.get_coords(), landscape.print_object(unit.get_coords()))
        unit.set_coords(coords[0], coords[1])
        space.enter_object(unit.get_coords(), unit.get_emoji())

class Slowed(Strategy):
    def action(self, space, landscape, unit, coords):
        if bool(random.choice([True, False])):
            space.delete_object(unit.get_coords(), landscape.print_object(unit.get_coords()))
            unit.set_coords(coords[0], coords[1])
            space.enter_object(unit.get_coords(), unit.get_emoji())

class Barrier(Strategy):
    def action(self, space, landscape, unit, coords):
        pass

class Death(Strategy):
    def action(self, space, landscape, unit, coords):
        pass

class Mover:
    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    
    def moving(self, space, landscape, unit, coords):
        self.strategy.action(space, landscape, unit, coords)

def go(space, landscape, unit, direction):
    coords = list(unit.get_coords())
    if direction == 'w': coords[1] -= 1
    elif direction == 'd': coords[0] += 1
    elif direction == 's': coords[1] += 1
    elif direction == 'a': coords[0] -= 1
    current_spot = landscape.print_object(unit.get_coords())
    next_spot = landscape.print_object(coords)
    mover = Mover()
    #if next_spot == landscape.get_barrier_emoji():
    #    mover.set_strategy(Barrier())
    #elif next_spot == landscape.get_death_emoji():
    #    mover.set_strategy(Death())
    if next_spot == landscape.get_slowed_emoji() and current_spot == landscape.get_ground_emoji():
        mover.set_strategy(Move())
    elif current_spot == landscape.get_slowed_emoji() and next_spot == landscape.get_slowed_emoji():
        mover.set_strategy(Slowed())
    elif current_spot == landscape.get_slowed_emoji() and next_spot == landscape.get_ground_emoji():
        mover.set_strategy(Slowed())
    elif current_spot == landscape.get_ground_emoji() and next_spot == landscape.get_ground_emoji():
        mover.set_strategy(Move())
    else:
        mover.set_strategy(Barrier())
    mover.moving(space, landscape, unit, coords)



