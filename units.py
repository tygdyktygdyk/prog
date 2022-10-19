class Unit:
    def __init__(self, x=6, y=6, h=10, ar=10, at=10):
        self.__x = x; self.__y = y; self.__health = h
        self.__armor = ar; self.__atack = at

    def move(self, direction):
        if direction == 'w':
            if self.__y > 0: self.__y -= 1
        elif direction == 'd':
            if self.__x < 12: self.__x += 1
        elif direction == 's':
            if self.__y < 12: self.__y += 1
        elif direction == 'a':
            if self.__x > 0: self.__x -= 1

    def get_coords(self):
        return self.__x, self.__y
