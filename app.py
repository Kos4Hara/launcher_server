from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Сервер для лаунчера работает!"

@app.route('/start_game', methods=['GET'])
def start_game():
    print("Получен запрос на запуск игры с клиента.")
    return jsonify({"status": "success", "message": "Игра успешно запущена!"})

@app.route('/download', methods=['GET'])
def download():
    print("Запрос на скачивание.")
    return jsonify({"status": "success", "message": "Скачивание началось!"})

@app.route('/update', methods=['GET'])
def update():
    print("Запрос на обновление.")
    return jsonify({"status": "success", "message": "Обновление началось!"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
