class Map:
    def __init__(self, s, l):
        self.__str = s
        self.__length = l
    
    def print_map(self):
        return self.__str
    
    def chage_length(self, l):
        self.__str = ('\U0001F332' * l + '\n') * l 
        self.__length = l
    
    def enter_object(self, coords, a):
        tmp = coords[0] + coords[1] * (self.__length + 1)
        self.__str = self.__str[:tmp] + a + self.__str[(tmp+1):]
    
    def delete_object(self, coords):
        tmp = coords[0] + coords[1] * (self.__length + 1)
        self.__str = self.__str[:tmp] + '\U0001F332' + self.__str[(tmp+1):]
