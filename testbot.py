import telebot



bot = telebot.TeleBot("5793642588:AAE6hNG_44UDkYLNwxaHSDQKIqPX4hqplPM")

row = "\U0001F33E"*13 + '\n'
map = row*13

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, map)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
