import telebot
from func import *
from gamespace import *
from units import *

bot = telebot.TeleBot("5793642588:AAE6hNG_44UDkYLNwxaHSDQKIqPX4hqplPM")
    
str_map = ('\U0001F332' * 13 + '\n') * 13
space = Space(str_map, 13)
kaktus = Unit()
space.enter_object(kaktus.get_coords(), '\U0001F335')

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'поехали':
        bot.send_message(message.chat.id, space.print_map())
    if message.text.lower() in ['w', 'd', 's', 'a']:
        move_unit(space, kaktus, message.text.lower())
        bot.send_message(message.chat.id, space.print_map())

bot.infinity_polling()
