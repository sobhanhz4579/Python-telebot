import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from product_info import *
from handler_s_welcome import *
from help import *
from handler_informationss import *
from handler_msg import *
from callback import *

TOKEN = '...'
SUPPORT_CHAT_ID = ...
bot = telebot.TeleBot(TOKEN)

user_details = {}


@bot.message_handler(commands=['start'])
def start_handler(message):
    send_welcome(message, bot)


@bot.callback_query_handler(func=lambda call: True)
def query_callback(call):
    callback_query(call)


@bot.message_handler(commands=['help'])
def help_handler(message):
    send_help(message, bot)


@bot.message_handler(commands=['information'])
def angabe_handler(message):
    send_informationen_plans(message, bot)


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    handle_message(message, bot)


if __name__ == '__main__':
    bot.polling()
