import os

from telebot.types import InlineKeyboardButton


class Config:
    BOT_TOKEN = os.environ['BOT_TOKEN']


def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = """Hello, {0}
This is the starter template for other bots built with <b>python</b>. 
No bots cooked so far.
Enjoy cooking with <a href = 'https://github.com/VadimCpp/pyfirstbotbot'>this template</a>!""".format(first_name)
    return text
