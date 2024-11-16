from flask import Flask, request, jsonify

app = Flask(__name__)

# Функция, обрабатывающая входящие сообщения и возвращающая ответ
def generate_response(user_message):
    # Логика генерации ответа
    return f"Вы сказали: {user_message}"

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.json
    user_message = data.get('message', '')
    response = generate_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
