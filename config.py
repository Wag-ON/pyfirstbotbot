import os
import dotenv
from telebot.types import InlineKeyboardButton

dotenv.load_dotenv()
class Config:
    MODE = os.getenv('MODE')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    URL = os.getenv('URL')


def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = """Привет, {0}
Это попытка модифицировать неофициального бота БФУ.
Вся разработка ведется в чате @frontendbasics.
Все что не делается - все к лучшему""".format(first_name)
    return text
