import telebot
from func import *
from map import *
from units import *

bot = telebot.TeleBot("5793642588:AAE6hNG_44UDkYLNwxaHSDQKIqPX4hqplPM")
    
str_map = ('\U0001F332' * 13 + '\n') * 13
map = Map(str_map, 13)
kaktus = Unit()
map.enter_object(kaktus.get_coords(), '\U0001F335')

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'поехали':
        bot.send_message(message.chat.id, map.print_map())
    if message.text.lower() in ['w', 'd', 's', 'a']:
        move_unit(map, kaktus, message.text.lower())
        bot.send_message(message.chat.id, map.print_map())

bot.infinity_polling()
