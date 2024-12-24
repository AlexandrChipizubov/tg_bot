import telebot
from telebot import types

# bot = telebot.TeleBot(open('token.txt', 'r').read())

# @bot.message_handler(commands = ['start'])

# def start(message):

#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("👋 Поздороваться")
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):

#     if message.text == '👋 Поздороваться':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
#         btn2 = types.KeyboardButton('Правила сайта')
#         btn3 = types.KeyboardButton('Советы по оформлению публикации')
#         markup.add(btn1, btn2, btn3)
#         bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup) #ответ бота

#     elif message.text == 'Правила сайта':
#         bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

#     elif message.text == 'Советы по оформлению публикации':
#         bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')

# bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть



# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)

# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("🇷🇺 Русский")
#     btn2 = types.KeyboardButton('🇬🇧 English')
#     markup.add(btn1, btn2)
#     bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)