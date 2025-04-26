'''https://web.telegram.org/a/#8081854859 - Ссылка на бота'''
import telebot
from telebot import types
import random
from datetime import datetime
import pytz

BOT_TOKEN = "8081854859:AAGmTAk0KPW-zSXtfb35YQBXLET7zJT90Vo"
MOSCOW_TIMEZONE = 'Europe/Moscow'

bot = telebot.TeleBot(BOT_TOKEN)


def create_main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
        types.KeyboardButton("Узнать время"),
        types.KeyboardButton("Рандомное число"),
        types.KeyboardButton("Мой ID")
    ]

    menu.add(*buttons)
    return menu


def get_current_moscow_time():
    timezone = pytz.timezone(MOSCOW_TIMEZONE)
    return datetime.now(timezone).strftime("%H:%M:%S")


def generate_random_number():
    return random.randint(1, 100)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "Привет! Я бот с полезными функциями. Выбери действие из меню:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=create_main_menu())


@bot.message_handler(content_types=['text'])
def handle_user_requests(message):
    user_message = message.text

    if user_message == "Узнать время":
        time = get_current_moscow_time()
        bot.send_message(message.chat.id, f"Текущее время по Москве: {time}")

    elif user_message == "Рандомное число":
        number = generate_random_number()
        bot.send_message(message.chat.id, f"Ваше случайное число: {number}")

    elif user_message == "Мой ID":
        user_id = message.from_user.id
        bot.send_message(message.chat.id, f"Ваш ID: {user_id}")

    else:
        error_text = "Не понимаю эту команду. Пожалуйста, используй кнопки меню."
        bot.send_message(message.chat.id, error_text, reply_markup=create_main_menu())


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)