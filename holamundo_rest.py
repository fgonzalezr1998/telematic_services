#! /usr/bin/env python

from flask import Flask
import json

app=Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"

@app.route('/user/<name>')
def user(name):
    return "Hola, " + name

if __name__ == '__main__':
    app.run(debug=True)

    exit(0)
