class Map:
    def __init__(self, s, l):
        self.str = s
        self.length = l
    
    def print_map(self):
        return self.str
    
    def chage_length(self, l):
        self.str = ('\U0001F332' * l + '\n') * l 
        self.length = l
    
    def enter_object(self, x, y, a):
        tmp = x + y * (self.length + 1)
        self.str = self.str[:tmp] + a + self.str[(tmp+1):]
    
    def delete_object(self, x, y):
        tmp = x + y * (self.length + 1)
        self.str = self.str[:tmp] + '\U0001F332' + self.str[(tmp+1):]
