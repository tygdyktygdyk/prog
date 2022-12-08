class Space:
    def __init__(self, s):
        self.__str = s
        self.__length = 13
    
    def print_map(self):
        return self.__str

    def print_object(self, coords):
        if 0 > coords[0] > self.__length and 0 > coords[0] > self.__length: 
            return False
        tmp = coords[0] + coords[1] * (self.__length + 1)
        return self.__str[tmp]
    
    def enter_object(self, coords, emoji):
        tmp = coords[0] + coords[1] * (self.__length + 1)
        self.__str = self.__str[:tmp] + emoji + self.__str[(tmp+1):]
    
    def delete_object(self, coords, ground):
        tmp = coords[0] + coords[1] * (self.__length + 1)
        self.__str = self.__str[:tmp] + ground + self.__str[(tmp+1):]
