import telebot
import logging
import json
from config import *
#from firebase import firebase

from flask import Flask, request

MODE = Config.MODE
TOKEN = Config.BOT_TOKEN
URL = Config.URL


# FireBase Account:
# Login: bfubot123@gmail.com
# Password: Firdu8-jantih-tanxon

# NOTE
# old jsonString
#jsonString = '{ "Group": "MO-2", "TimeTable":{"Day":[ {"DayName":"Вторник", "time": "15-20","Cab": "(ауд. 231)", "Lesson": "лекция Python"}, {"DayName":"Среда", "Подгруппа": [{"Номер":"(2я подгруппа)", "time":"10-10", "Cab":"(ауд. 235)",  "Lesson": "лаба Python"}, {"Номер":"(3я подгруппа)","time":"12-00", "Cab": "(ауд. 235)", "Lesson":"лаба Python"}, {"Номер":"(1я подгруппа)", "time":"13-40", "Cab":"(ауд. 230)", "Lesson": "лаба Python"} ]} ]} }'

# firebase = firebase.FirebaseApplication("https://bfubot.firebaseio.com/", None)
# jsonString_pm4='{ "Group": "ПМ-4", "TimeTable":{"Day":[  {"DayName":"Пятница", "Подгруппа":[{"Номер":"(1я подгруппа)", "time":"10-10", "Cab":"(ауд. 230А. Вход через 230 ауд.)", "Lesson": "лаба Python"},{"time":"12-00", "Cab":"(ауд.118)", "Lesson": "лекция Python"},{"Номер":"(2я подгруппа)", "time":"13-40", "Cab":"(ауд. 214)", "Lesson": "лаба Python"} ]} ]} }'
# result = firebase.get('/bfubot/Schedule', '')
# result = str(result)
# count = 0
# j = 0
# i = 0
# while count < 3:
#     if result[i] == "'":
#         count += 1
#         j = i + 1
#     i += 1
# l = int(len(result) - 2)
# result = result[:l] + ''
# result = '' + result[j:]
# jsonString = result
#
# obj = json.loads(jsonString)
# obj_pm4 =json.loads(jsonString_pm4)



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Ну это по классике, логи

bot = telebot.TeleBot(Config.BOT_TOKEN)  # Создает объект класса "TeleBot", то есть нашего бота
def init_server():
	server = Flask(__name__)

	# Инициализирует webhook
	@server.route("/")
	def webhook():
		bot.remove_webhook()
		bot.set_webhook(url=URL + TOKEN)
		return "!", 200

	# Обработывает события
	@server.route('/' + TOKEN, methods=['POST'])
	def getMessage():
		bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
		return "!", 200

	return server

def printSchedule(bot, message, groupNo):

    output = "Группа " + obj["Group"] + "\n\n"

    if groupNo == "/mo2":

        i = 0
        day = obj["TimeTable"]['Day']
        for i in range(2):
            if i == 0:
                output += "*" + day[i]["DayName"] + "*\n" + day[i]['time'] + ' ' + day[i]['Cab'] + ' ' + day[i]['Lesson'] + '\n\n'
            if i == 1:
                output += '*' + day[i]["DayName"] + '*\n'

        i = 0

        for i in range(3):
            output += day[1]["Подгруппа"][i]["time"] + " " + day[1]["Подгруппа"][i]["Cab"] + " " + day[1]["Подгруппа"][i]['Lesson'] + ' ' + day[1]["Подгруппа"][i]["Номер"] + "\n"

        bot.send_message(message.chat.id, output, parse_mode="Markdown")




    elif groupNo == "/pm4":
        bot.send_message(message.chat.id,
                         "Группа " + obj_pm4["Group"] + "\n\n" +
                         "*" + obj_pm4['TimeTable']["Day"][0]["DayName"] + "*\n"  +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][0]["time"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][0]["Cab"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][0]['Lesson'] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][0]["Номер"] + '\n' +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][1]["time"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][1]["Cab"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][1]["Lesson"] + '\n' +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][2]["time"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][2]["Cab"] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][2]['Lesson'] + " " +
                         obj_pm4['TimeTable']["Day"][0]["Подгруппа"][2]["Номер"] + '\n', parse_mode="Markdown")

    elif message.chat.id > 0:
        bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',
                         disable_web_page_preview=True)  # Отправляет авто сообщение


@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])  # декоратор который заставляет пользователя реагировать на новые сообщения

@bot.message_handler(commands=['mo2'])

def sending_auto2(message):

    #printSchedule(bot, message, message.text)
    bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',
                     disable_web_page_preview=True)  # Отправляет авто сообщение

    # NOTE
    # Не отправляем сообщения в общие чаты.
    # else:
    # bot.send_message(chat_id=message.chat.id, text='Это сообщение в чат', parse_mode='html',disable_web_page_preview=True)
#sending_auto2(message)

if __name__ == '__main__':
    logging.info("Selected mode " + MODE)
    if MODE == "debug":
        bot.remove_webhook()
        bot.polling() # Заставляет бота получать уведомления о новых сообщениях
    else:
		# Сервер необходим для работы webhook
        server = init_server()
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))
