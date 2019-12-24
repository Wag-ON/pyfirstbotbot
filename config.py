import os

from telebot.types import InlineKeyboardButton


class Config:
    BOT_TOKEN = os.environ['BOT_TOKEN']


def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = """Привет, {0}
Ну вот мы и запустили неофициального бота БФУ.
Вся разработка ведется в чате @frontendbasics.
А пока запасайтесь попкорном 🍿""".format(first_name)
    return text
