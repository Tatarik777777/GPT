from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Получаем токен бота из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('8065019894:AAFxs4L3BrBOhJbkXAjcjtR0aDGZcymWO1I')
BOT_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Извлечение текста сообщения и идентификатора чата
    message_text = data.get('message', {}).get('text', '')
    chat_id = data.get('message', {}).get('chat', {}).get('id')

    # Проверка, что получено сообщение и идентификатор чата
    if message_text and chat_id:
        response_text = generate_response(message_text)
        send_message(chat_id, response_text)

    return '', 200

def generate_response(message):
    # Логика ответа на сообщения
    if "привет" in message.lower():
        return "Привет! Как я могу помочь?"
    elif "как дела" in message.lower():
        return "У меня все хорошо, спасибо! А у вас?"
    else:
        return "Извините, я не понимаю ваш запрос."

def send_message(chat_id, text):
    # Отправка сообщения обратно в Telegram
    requests.post(BOT_API_URL, json={'chat_id': chat_id, 'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
