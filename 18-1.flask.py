# Использование модуля Flask, запускаещь программу,
# в браузере вводишь 127.0.0.1:8000- и ты в инете!типа)))
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
app.run(port = '8000')
