from flask import Flask, render_template
from random import randint
from time import sleep
import os
import sys

app = Flask(__name__)


@app.route('/healthz/live')
def liveness():
    sleep(randint(1, 2))
    return 'OK', 200


@app.route('/healthz/ready')
def readiness():
    sleep(randint(1, 2))
    return 'OK', 200


@app.route('/error-502')
def error_502():
    sleep(randint(5, 10))
    return render_template('index.html', message='502 Bad gateway!'), 502


@app.route('/error-500')
def error():
    sleep(randint(1, 5))
    return render_template('index.html', message='Panic panic!'), 500


@app.route('/')
def hello_world():
    sleep(randint(1, 5))
    return render_template('index.html', message='Hello, World!')


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
