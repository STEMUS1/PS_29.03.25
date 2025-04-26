import telebot
import requests
import random
from telebot import types

BOT_TOKEN = "7538591484:AAEaIh9GXfs55Tw2G1i78-GNRu9wlqZLU8k"
bot = telebot.TeleBot(BOT_TOKEN)

WEATHER_API_KEY = "57a446a424d57ba46f036f676147c671"
CITY = "Moscow"

sticker_ids = [
    "CAACAgIAAxkBAAEKjpxlq65_7-lD7xK-rA_wPj-d7UqS2wACDQADwDZPEzB-jKbX6wGLwQ",
    "CAACAgIAAxkBAAEKjp5lq66i7_2Qc_xG2Sg4-6G2y0i9lgACDwADwDZPEy87_k-9-9WLwQ",
    "CAACAgIAAxkBAAEKjqBlq6696FvXn_gW8jJjG94i5gL90wACDQADwDZPEzT-yB35NQL2wQ",
    "CAACAgIAAxkBAAEKjqJlq67N-89eP1t5kYd9uL10JkH2ggACDgADwDZPEzGkG9q-qJCLwQ",
    "CAACAgIAAxkBAAEKjqRlq67b6X_pYlP56B1l5iWjX1W3lQACDAADwDZPEycVvJjX2gMLwQ",
    "CAACAgIAAxkBAAEKjqZlq67vO1aXh-z57n1hP7r40U7t2wACDQADwDZPEz9nK-bU9VPLwQ",
]

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except (KeyError, TypeError):
        return None, "Ошибка получения данных о погоде"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton("Текущая погода")
    sticker_button = types.KeyboardButton("Стикер")
    markup.add(weather_button, sticker_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать погоду или получить стикер.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def hello(message):
    bot.reply_to(message, "Привет, человек")

@bot.message_handler(func=lambda message: message.text == "Текущая погода")
def weather(message):
    temperature, description = get_weather(CITY)
    if temperature is not None:
        bot.send_message(message.chat.id, f"Погода в городе {CITY}: {temperature:.1f}°C, {description}")
    else:
        bot.send_message(message.chat.id, description)

@bot.message_handler(func=lambda message: message.text == "Стикер")
def sticker(message):
    random_sticker = random.choice(sticker_ids)
    bot.send_sticker(message.chat.id, random_sticker)

if __name__ == '__main__':
    bot.infinity_polling()