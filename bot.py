import telebot
from telebot import types
import config
import API as api
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def first_button(update : Update, context: CallbackContext):
    update.message.reply_text(text = 'Отправь мне локацию или координаты (долгота, широта):')

def second_button(update : Update, context: CallbackContext ):
    reply_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text = 'Москва')],
        [KeyboardButton(text='Санкт-Петербург')],
        [KeyboardButton(text='Краснодар')],
        [KeyboardButton(text='Сочи')],
        [KeyboardButton(text='Нижний Новгород')],
        [KeyboardButton(text='Калининград')],
        [KeyboardButton(text='Томск')],
        [KeyboardButton(text='Тюмень')],
        [KeyboardButton(text='Определить погоду по геопозиции')],
    ])
    update.message.reply_text(text = 'Выберите название города: ', reply_markup = reply_keyboard)

def start(update, context):
    reply_keyboard = ReplyKeyboardMarkup(keyboard=[
                                                [KeyboardButton(text='Определить погоду по геопозиции')],
                                                [KeyboardButton(text = 'Определить по названию города')]
                                                ], resize_keyboard=True)
    update.message.reply_text(text='Добро пожаловать в наш бот\nВыберите ваше действие:', reply_markup=reply_keyboard)
    text = update.message.text

#Эта функция будет использоваться, если пользователь послал в бота любой текст.
#Мы ожидаем координаты, но если прийдет что-то другое не страшно, ведь мы описали в функции получения адреса возвращение ошибки в случае чего.
def text(update: Update, context: CallbackContext):
    text = update.message.text
    #отправляем текст в нашу функцио получения адреса из координат
    #вовщращаем результат пользователю в боте
    if text == 'Определить погоду по геопозиции':
        return first_button(update, context)
    if text == 'Определить по названию города':
        return second_button(update, context)
    text = update.message.text
    if text == 'Москва':
        answer = api.function_for_all("http://api.openweathermap.org/data/2.5/weather?q=Moscow&mode=xm"
                                          "l&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589")
        update.message.reply_text(answer)
    elif text == 'Санкт-Петербург':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5'
                                      '/weather?q=Saint%20Petersburg&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Краснодар':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weather?q=Krasnodar'
                                      '&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Сочи':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weather?q=Sochi&mode=xml'
                                      '&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Нижний Новгород':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weathe'
                                      'r?q=Nizhny%20Novgorod&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Калининград':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weather?q=Kaliningra'
                                      'd&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Томск':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weather?q'
                                      '=Tomsk&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
    elif text == 'Тюмень':
        answer = api.function_for_all('http://api.openweathermap.org/data/2.5/weather?q='
                                      'Tyumen&mode=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589')
        update.message.reply_text(answer)
#Эта функция будет использоваться, если пользователь послал локацию.
def location(update, context):
    message = update.message
    current_position = (message.location.longitude, message.location.latitude)
    answer = api.get_it(current_position[1],current_position[0])
    update.message.reply_text(answer)

#Это основная функция, где запускается наш бот
def main():
    #создаем бота и указываем его токен
    updater = Updater(config.token, use_context=True)
    #создаем регистратор событий, который будет понимать, что сделал пользователь и на какую функцию надо переключиться.
    dispatcher = updater.dispatcher

    #регистрируем команду /start и говорим, что после нее надо использовать функцию def start
    dispatcher.add_handler(CommandHandler("start", start))
    #регистрируем получение текста и говорим, что после нее надо использовать функцию def text
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    #регистрируем получение локации и говорим, что после нее надо использовать функцию def location
    dispatcher.add_handler(MessageHandler(Filters.location, location))
    #запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    #запускаем функцию def main
    main()
