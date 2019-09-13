TOKEN = '829333255:AAH7B6hqC6IAaNqaw6b0QhylKx_sNq7Styc'

def autosending_text(bot, message):
	first_name = bot.get_chat(message.chat.id).first_name
	text = """Hello, {0}
This is the starter template for other bots built with python. 

No bots cooked so far.


Enjoy cooking with <a href = 'https://github.com/LimiO/TutorialHeroku'>this template</a>!""".format(first_name)
	return text
