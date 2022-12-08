from abc import ABC, abstractmethod

# краткие названия всех emoji
tr = '\U0001F332' # ель
wb = '\U0001F578'
st = '\U0001FAA8' # камень
br = '\U0001F6A7' # строительное огражедение

sn = '\U0001F7E8' # песок
gr = '\U0001F7E9' # трава
bl = '\U00002B1B' # асфальт

class AbstractLandscape(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_map(self):
        pass

    @abstractmethod
    def print_object(self, coords):
        pass

    @abstractmethod
    def print_object(self, coords, emoji):
        pass

    @abstractmethod
    def get_ground_emoji(self):
        pass

    @abstractmethod
    def get_barrier_emoji(self):
        pass

    @abstractmethod
    def get_death_emoji(self):
        pass

    @abstractmethod
    def get_slowed_emoji(self):
        pass

class ForestLandscape(AbstractLandscape):
    def __init__(self):
        self.__str_map = tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+'\n'+\
                         tr+gr+gr+gr+gr+gr+gr+gr+tr+tr+tr+tr+tr+'\n'+\
                         tr+gr+gr+tr+tr+gr+gr+tr+tr+tr+tr+tr+tr+'\n'+\
                         tr+gr+gr+gr+tr+gr+gr+tr+tr+tr+tr+tr+tr+'\n'+\
                         tr+gr+gr+gr+gr+gr+gr+gr+tr+tr+tr+gr+tr+'\n'+\
                         tr+gr+gr+gr+gr+gr+gr+gr+gr+tr+tr+gr+tr+'\n'+\
                         tr+gr+gr+tr+gr+gr+gr+gr+gr+gr+gr+gr+tr+'\n'+\
                         tr+wb+wb+tr+gr+gr+gr+gr+gr+tr+tr+gr+tr+'\n'+\
                         tr+wb+tr+tr+gr+gr+gr+tr+tr+tr+tr+gr+tr+'\n'+\
                         tr+wb+wb+tr+wb+wb+tr+tr+tr+tr+gr+gr+tr+'\n'+\
                         tr+wb+wb+wb+wb+wb+gr+tr+gr+gr+gr+gr+tr+'\n'+\
                         tr+wb+wb+wb+wb+wb+gr+gr+gr+gr+gr+gr+tr+'\n'+\
                         tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+tr+'\n'
        self.__ground = gr
        self.__barrier = tr
        self.__death = 'wb'
        self.__slowed = wb

    def get_map(self):
        return self.__str_map

    def print_object(self, coords):
        if 0 > coords[0] > 13 and 0 > coords[0] > 13:
            return False
        tmp = coords[0] + coords[1] * 14
        return self.__str_map[tmp]

    def enter_object(self, coords, emoji):
        tmp = coords[0] + coords[1] * 14
        self.__str_map = self.__str_map[:tmp] + emoji + self.__str_map[(tmp+1):]
    
    def get_ground_emoji(self):
        return self.__ground

    def get_barrier_emoji(self):
        return self.__barrier

    def get_death_emoji(self):
        return self.__death

    def get_slowed_emoji(self):
        return self.__slowed
