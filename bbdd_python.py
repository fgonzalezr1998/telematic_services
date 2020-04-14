#! /usr/bin/env python

import sqlite3 as sql
import sys

#CONSTS:
MinMainMenuItem = 1
MaxMainMenuItem = 4

class SQLExecutor():
    def __init__(self, bdd_path):
        self.conn_bd = sql.connect(bdd_path)
        self.cursor = self.conn_bd.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn_bd.close()

    #PUBLIC METHODS:
    def execute(self, action):

        if(action == 1):
            print("Mostrar datos")
        elif(action == 2):
            print("Modificar cliente")
        else:
            print("Modificar coche")

def action_chosen():

    ok = True
    n = 0
    try:

        n = int(input("\nIndique una Accion: "))

    except NameError:
        ok = False
    except SyntaxError:
        ok = False

    if(n < MinMainMenuItem or n > MaxMainMenuItem):
        ok = False

    if(ok):
        return n
    else:
        return -1

def main_menu():

    print("1) Realizar Consulta")
    print("2) Modificar Cliente")
    print("3) Modificar Coche")
    print("4) Salir")

if __name__ == "__main__":

    executor = SQLExecutor("./practica_bbdd/practica_taller.sqlite")
    n_action = 0

    while(n_action != MaxMainMenuItem):

        main_menu()                 #Display main menu
        n_action = action_chosen()  #Read action user choose
        if(n_action < 0):
            print("\n[ERROR] bad entry\n")
            continue

        if(n_action == MaxMainMenuItem):
            continue

        #if everything ok, execute action
        executor.execute(n_action)

    exit(0)
