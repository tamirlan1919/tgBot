import telebot
from telebot import types
from telebot.types import Message, CallbackQuery
from config import TOKEN
from database.models import make_table_user
from database.crud import insert_to_table_user, select_user_by_id
import datetime

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message: Message):
    user = select_user_by_id(message.from_user.id)
    print(user)
    if user is None:
        bot.send_message(message.chat.id, 'Будем знакомы')
        insert_to_table_user(message.from_user.id, message.from_user.username,
                             datetime.datetime.now())
    else:
        bot.send_message(message.chat.id, 'Так я тебя знаю друг')


if __name__ == '__main__':
    make_table_user()
    bot.polling(none_stop=True)

