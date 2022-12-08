import random
import telebot
from func import *
from gamespace import *
from units import *
from landscape import *
from bases import *

bot = telebot.TeleBot("5882178523:AAENyEZLtMDyodiY_MZz8-xUXylaRVbvb9g")
    
List_Of_Units = []

forest = ForestLandscape()

space = Space(forest.get_map())
create_unit(ConcreteFactory2(), space, List_Of_Units, 'C', 6, 6)

base = add_new_base(space, 3, 3)
forest.enter_object([3, 3], base.get_emoji())

@bot.message_handler(content_types=['text'])
def get_text(message):
    command = message.text.lower()
    if command == 'start':
        bot.send_message(message.chat.id, space.print_map())
    elif command == 'q':
        for unit in List_Of_Units[1:]:
            go(space, forest, unit, random.choice(['w', 'd', 's', 'a']))
        bot.send_message(message.chat.id, space.print_map())
    elif command in ['w', 'd', 's', 'a']:
        go(space, forest, List_Of_Units[0], command)
        for unit in List_Of_Units[1:]:
            go(space, forest, unit, random.choice(['w', 'd', 's', 'a']))
        trigger(space, List_Of_Units, base)
        bot.send_message(message.chat.id, space.print_map())
    elif command[:command.find(' ')] == 'delete':
        space.delete_object(list(map(int, command[(command.find(' ')+1):].split())))
        bot.send_message(message.chat.id, space.print_map())
    elif command[:command.find(' ')] == 'reload':
        space.delete_object(you.get_coords())
        you.change_coords(6, 6)
        space.enter_object(you.get_coords(), you.get_emoji())
        bot.send_message(message.chat.id, space.print_map())
    elif command[:command.find(' ')] == 'change_size':
        space.change_length(int(command[(command.find(' ')+1):]))
        bot.send_message(message.chat.id, space.print_map())


bot.infinity_polling()
