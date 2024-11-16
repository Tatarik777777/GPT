from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8065019894:AAFxs4L3BrBOhJbkXAjcjtR0aDGZcymWO1I'
BOT_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Получение текста сообщения из Telegram
    message_text = data['message']['text']
    chat_id = data['message']['chat']['id']

    # Здесь вы можете обрабатывать сообщение и создавать ответ
    response_text = process_message(message_text)

    # Отправка ответа обратно в Telegram
    requests.post(BOT_API_URL, json={'chat_id': chat_id, 'text': response_text})

    return '', 200

def process_message(message):
    # Пример простой обработки сообщения
    if "привет" in message.lower():
        return "Привет! Как я могу помочь?"
    else:
        return f"Вы сказали: {message}"

if __name__ == '__main__':
    app.run(port=5000)
