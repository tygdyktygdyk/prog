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
        

class Unit:
    def __init__(self, x=6, y=6, h=10, ar=10, at=10):
        self.x = x; self.y = y; self.health = h
        self.armor = ar; self.atack = at

    def move(self, direction):
        if direction == 'w':
            if self.y > 0: self.y -= 1
        elif direction == 'd':
            if self.x < 12: self.x += 1
        elif direction == 's':
            if self.y < 12: self.y += 1
        elif direction == 'a':
            if self.x > 0: self.x -= 1
