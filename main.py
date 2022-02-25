import telebot
from telebot import types

bot = telebot.TeleBot('5259573299:AAE3tpt9ZOekyxOsfgOKbpIk2qbTQpd1JKo')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Добро пожаловать, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')





bot.polling(none_stop=True)

