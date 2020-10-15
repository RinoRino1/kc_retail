import os
import json
import telebot
import commercial

TOKEN = '1338083803:AAG2JxFfHDXTkDj8bL75Jxnb7KiSxx_3F_Y'

bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('pegasus', 'air arabia', 'etm', 'amadeus', 'content rail', 'fly dubai', 'crm')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, мой юный агент! не удивляйся, этот бот поможет тебе быстрее найти нужное инфо.Если нажимать внизу на кнопки, можно получить сразу ссылку на систему. нажми на команду /info',reply_markup=keyboard)

@bot.message_handler(commands=['end'])
def end_message(message):
    bot.send_message(message.chat.id, 'я закругляюсь, до встречи!')

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, 'команды которыми можно управлять /start - начало бота, /commercial - ком курс, /end - конец бота')

@bot.message_handler(commands=['commercial'])
def commercial_message(message):
    for x in commercial.get_items_info(commercial.get_page_soup('https://concept.kg/news/2/')):
        bot.send_message(message.chat.id, f'{x[0]}: {x[1]}')




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in ['pegasus', 'пегасус', 'PS']:
        bot.send_message(message.chat.id, 'https://agency.flypgs.com/Login.jsp?activeLanguage=RU')
    if message.text.lower() in ['air arabia', 'эйр арабия', 'G9']:
        bot.send_message(message.chat.id, 'https://reservations.airarabia.com/xbe/#')
    if message.text.lower() in ['etm', 'етм']:
        bot.send_message(message.chat.id, 'https://etix.concept.kg/home')
    if message.text.lower() in ['amadeus', 'амадеус', 'амадэус']:
        bot.send_message(message.chat.id, 'https://www.sellingplatformconnect.amadeus.com/LoginService/login.jsp?SITE=LOGINURL&LANGUAGE=GB&event=LOGIN_LOGOUT')
    if message.text.lower() in ['content rail', 'контент рейл']:
        bot.send_message(message.chat.id, 'https://contentrail.com')
    if message.text.lower() in ['fly dubai', 'флай дубай', 'FZ']:
        bot.send_message(message.chat.id, 'https://ta.flydubai.com/en/user/signin/?ReturnUrl=%2fen%2fuser%2fmakebooking%2f%3farea%3d&area=')
    elif message.text.lower() in ['crm', 'срм']:
        bot.send_message(message.chat.id, 'https://concept.cisamadeus.com/remark/remark_update.php?sign=0019ma')























bot.polling()