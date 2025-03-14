from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return

@app.route('/start_game')
def start_game():
    return "Игра запущена!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
