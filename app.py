from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Добро пожаловать в лаунчер игры!"

@app.route('/start_game')
def start_game():
    print("Игра запущена!")  # Лог на сервере
    return jsonify({"status": "success", "message": "Игра запущена!"})

@app.route('/download')
def download():
    print("Началась загрузка!")
    return jsonify({"status": "success", "message": "Загрузка началась!"})

@app.route('/update')
def update():
    print("Обновление началось!")
    return jsonify({"status": "success", "message": "Обновление началось!"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
