from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/start_game')
def start_game():
    print("Запрос на запуск игры получен!")
    return "Игра запускается!"

@app.route('/download')
def download():
    print("Запрос на скачивание!")
    return "Начато скачивание."

@app.route('/update')
def update():
    print("Запрос на обновление!")
    return "Обновление началось."

@app.route('/exit_app')
def exit_app():
    print("Запрос на выход!")
    return "Выход из приложения."

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
