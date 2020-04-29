#! /usr/bin/python

import json
import flask
import os
import sqlite3
from werkzeug.exceptions import BadRequestKeyError

#Consts:
BBDDPath = "rest_sqlite.sqlite"

conn_bd = None
cursor = None

def response():
    sql = "SELECT * FROM Comments"
    cursor.execute(sql)
    comments = cursor.fetchall()

    lst = []
    for i in comments:
        l = list(i)
        elem = {"title": l[1], "body": l[2], "userId": l[3]}
        lst.append(elem)

    return lst

def response_n(n):

    try:
        n = int(n)
    except ValueError:
        print("[ERROR] Invalid Value!")
        return
    #SQL query:
    sql = "SELECT * FROM Comments"
    cursor.execute(sql)
    comments = cursor.fetchall()

    lst = []
    for i in comments:
        l = list(i)
        if(l[0] == int(n)):
            elem = {"title": l[1], "body": l[2], "userId": l[3]}
            lst.append(elem)

    return lst

def response_users():

    #SQL query:
    sql = "SELECT * FROM Users"
    cursor.execute(sql)
    users = cursor.fetchall()

    lst = []
    for i in users:
        l = list(i)
        elem = {"name": l[1], "username": l[2]}
        lst.append(elem)

    return lst

def response_userId(n):
    try:
        n = int(n)
    except ValueError:
        print("[ERROR] Invalid Value!")
        return
    #SQL query:
    sql = "SELECT * FROM Comments"
    cursor.execute(sql)
    comments = cursor.fetchall()

    lst = []
    for i in comments:
        l = list(i)
        if(l[3] == int(n)):
            elem = {"title": l[1], "body": l[2], "userId": l[3]}
            lst.append(elem)

    return lst

app = flask.Flask(__name__)

@app.route('/posts')
def posts():
    request = flask.request.args
    print(request)
    if len(request) > 0:
        try:
            id = request['userId']
        except BadRequestKeyError:
            print("[ERROR] Requested resource doesn't exist!")
            return "[ERROR] Requested resource doesn't exist!"
        respuesta = response_userId(id)
        return json.dumps(respuesta, True, 4)
    else:
        respuesta = response()
        return json.dumps(respuesta, True, 4)


@app.route('/posts/<n>')
def posts_n(n):
    respuesta = response_n(n)
    return json.dumps(respuesta, True, 4)

@app.route('/users')
def users():
    respuesta = response_users()
    return json.dumps(respuesta, True, 4)


if __name__ == '__main__':

    if(not os.path.isfile(BBDDPath)):
        sys.exit(1)
    conn_bd = sqlite3.connect(BBDDPath, check_same_thread=False)
    cursor = conn_bd.cursor()

    app.run(debug=True)

    exit(0)
