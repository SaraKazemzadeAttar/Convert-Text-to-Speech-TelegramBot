import telebot
import os
import logging
from gtts import gtts

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id , "Please send me a text and I will read it for you!")


@bot.message_handler(func = lambda message: True)
def text_to_Speech(message):
    text = message.text
    file_name = "voices/output.mp3"
    output = gtts(text = text , lang="en" , tld = 'com.au')
    output.save(file_name)
    bot.send_voice(chat_id = message.chat.id , voice = open(file_name, 'rb') , caption = text , reply_to_message_id= message.id)
bot.infinity_polling()