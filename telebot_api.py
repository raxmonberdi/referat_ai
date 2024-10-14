import telebot
from ai_sorov import gpt_sorov
from doc_creator import doc_creator
from dotenv import dotenv_values
from users_functions import new_user
config = dotenv_values(".env")

bot = telebot.TeleBot(config["TELEGRAM_API"])



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	user_id = message.from_user.id
	bot.reply_to(message, f"Your user ID is {user_id}")


@bot.message_handler(commands=['yarat'])
def doc_yarat(message):
	user_id = message.from_user.id
	new_user(user_input=user_id)
	bot.reply_to(message, "Sizga 5 ta limit ajiratildi")
	

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	user_id = message.from_user.id
	refarat_mavzusi = message.text
	refarat_izohi=gpt_sorov(refarat_mavzusi)
	print("1-bosqich")
	doc_creator(refarat_mavzusi,refarat_izohi)
	doc=open("./generated_doc.docx", "rb")
	print("2-bosqich")
	bot.send_document(message.chat.id, doc)
	print("tugadi")


bot.infinity_polling()

# print(config)