import os
import telebot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print(f"Получена команда /start от пользователя {message.chat.id}")
    bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name} я твой менеджер паролей. Чем я могу помочь?")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.chat.id, "Введите название соцсети")


if __name__ == '__main__':
    print("Бот запущен и ожидает сообщений...")
    bot.remove_webhook()
    bot.infinity_polling()
