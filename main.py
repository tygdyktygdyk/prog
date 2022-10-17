import telebot

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
        self.x = x
        self.y = y
        self.health = h
        self.armor = ar
        self.atack = at

    def move(self, direction):
        if direction == 'w':
            if self.y > 0: self.y -= 1
        elif direction == 'd':
            if self.x < 12: self.x += 1
        elif direction == 's':
            if self.y < 12: self.y += 1
        elif direction == 'a':
            if self.x > 0: self.x -= 1

def move_unit(map, kaktus, direction):
    while(direction != 'e'):
        map.delete_object(kaktus.x, kaktus.y)
        kaktus.move(direction)
        map.enter_object(kaktus.x, kaktus.y, '\U0001F335')
        map.print_map()
        direction = input('direction - ')

bot = telebot.TeleBot("5793642588:AAE6hNG_44UDkYLNwxaHSDQKIqPX4hqplPM")

    
str_map = ('\U0001F332' * 13 + '\n') * 13
map = Map(str_map, 13)
map.enter_object(6, 6, '\U0001F335')
kaktus = Unit()

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'поехали':
        bot.send_message(message.chat.id, map.print_map())
    if message.text.lower() in ['w', 'd', 's', 'a']:
        map.delete_object(kaktus.x, kaktus.y)
        kaktus.move(message.text.lower())
        map.enter_object(kaktus.x, kaktus.y, '\U0001F335')
        bot.send_message(message.chat.id, map.print_map())

#move_unit(map, kaktus, input('direction - '))
bot.infinity_polling()
