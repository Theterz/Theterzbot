import telebot
import random
import glob
from requests import get
from telebot import types
mm = types.ReplyKeyboardMarkup(row_width=2)
button1 = types.KeyboardButton(" Привет")
button2 = types.KeyboardButton(" Хочу фото")
button3 = types.KeyboardButton(" Ещё фото")
button4 = types.KeyboardButton(" Назад")
mm.add(button1,button2,button3)
bot = telebot.TeleBot('923051792:AAEcFCvKm-9jeSXOh1eEqVwzkp0nzeYnLPM')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Если ты видишь это сообщения то я блять не зря просидел до 7 утра), и да привет, {message.from_user.first_name}', reply_markup=mm)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
       bot.send_message(message.chat.id, 'Привет солнышко❤️')
    if message.text == 'Хочу фото':
       bot.send_photo(message.chat.id, get("https://tambahinfo.files.wordpress.com/2012/07/20323.jpg?w=400").content)
    if message.text == 'Ещё фото':
       files = glob.glob('*.jpg')
       with open(random.choice(files), 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
bot.polling() 