#! /usr/bin/env python

import sqlite3
import sys
import os

#CONSTS:
MinMainMenuItem = 1
MaxMainMenuItem = 4

MinDataMenu = 1
MaxDataMenu = 5

MinClientMenu = 1
MaxClientMenu = 3

MinCarMenu = 1
MaxCarMenu = 3

class SQLExecutor():
    def __init__(self, bdd_path):
        if(not os.path.isfile(bdd_path)):
            sys.exit(1)
        self.conn_bd = sqlite3.connect(bdd_path)
        self.cursor = self.conn_bd.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn_bd.close()

    #PUBLIC METHODS:
    def execute(self, action):

        if(action == 1):
            self.show_data_()
        elif(action == 2):
            self.change_client_()
        else:
            self.change_car_()

    #PRIVATE METHODS:

    def change_client_(self):
        #Print submenu
        self.show_change_client_menu_()
        #Read action
        try:
            n_action = int(input("\nIndique una Accion: "))
        except NameError:
            sys.exit("\n[ERROR] bad entry\n")
        except SyntaxError:
            sys.exit("\n[ERROR] bad entry\n")
        except EOFError:
            sys.exit("\nQUE HACES METIENDO EOF?\n")
        if(n_action < MinClientMenu or n_action > MaxClientMenu):
            sys.exit("\n[ERROR] bad entry\n")

        self.make_change_client_query_(n_action)

    def change_car_(self):
        #Print submenu
        self.show_change_car_menu_()
        #Read action
        try:
            n_action = int(input("\nIndique una Accion: "))
        except NameError:
            sys.exit("\n[ERROR] bad entry\n")
        except SyntaxError:
            sys.exit("\n[ERROR] bad entry\n")
        except EOFError:
            sys.exit("\nQUE HACES METIENDO EOF?\n")
        if(n_action < MinCarMenu or n_action > MaxCarMenu):
            sys.exit("\n[ERROR] bad entry\n")

        self.make_change_car_query_(n_action)

    def show_data_(self):
        #Print submenu
        self.show_data_menu_()
        #Read action
        try:
            n_action = int(input("\nIndique una Accion: "))
        except NameError:
            sys.exit("\n[ERROR] bad entry\n")
        except SyntaxError:
            sys.exit("\n[ERROR] bad entry\n")
        except EOFError:
            sys.exit("\nQUE HACES METIENDO EOF?\n")

        if(n_action < MinDataMenu or n_action > MaxDataMenu):
            sys.exit("\n[ERROR] bad entry\n")

        sql = self.show_data_query_(n_action)
        self.cursor.execute(sql) #Execute query
        self.print_table_()     # print data returned properly

    def make_change_client_query_(self, n_action):
        if(n_action == 1):
            dni, n, a1, a2, tfno, dir = self.get_client_data_()
            sql = "INSERT INTO Clientes VALUES (?, ?, ?, ?, ?, ?)"
            args = (dni, n, a1, a2, tfno, dir)
            #self.cursor.execute(sql, (dni, n, a1, a2, tfno, dir)) #Execute query

        else:
            try:
                dni = raw_input("DNI: ")
            except EOFError:
                sys.exit("\nQUE HACES METIENDO EOF?\n")
            sql = "SELECT DNI FROM Clientes WHERE DNI = ?"
            self.cursor.execute(sql, (dni,))
            rd = self.cursor.fetchall()
            if(len(rd) == 0):
                print("[ERROR] Value doesn't exist!")
                return

            if(n_action == 2):
                print("\nNuevos Datos:")
                dni, n, a1, a2, tfno, dir = self.get_client_data_()

                sql = "UPDATE Clientes SET DNI = ?, Nombre = ?, Apellido1 = ?, \
                Apellido2 = ?, Telefono = ?, Direccion = ? WHERE DNI = ?"
                args = (dni, n, a1, a2, tfno, dir, rd[0][0])
            else:
                sql = "DELETE FROM Clientes WHERE DNI = ?"
                args = (dni,)
        try:
            self.cursor.execute(sql, args)
        except sqlite3.IntegrityError:
            print("\n[ERROR] There was an error modifying database!\n")

        self.conn_bd.commit()   #commit changes
        print("\n[WARN]Database Modified!\n")

    def make_change_car_query_(self, n_action):
        if(n_action == 1):
            mar, mod, mat, dni = self.get_car_data_()
            sql = "INSERT INTO Automoviles VALUES (?, ?, ?, ?, ?)"
            args = (None, mar, mod, mat, dni)

        else:
            mar, mod, mat, dni = self.get_car_data_()
            sql = "SELECT ID FROM Automoviles WHERE Marca = ? and Modelo = ? and \
            Matricula = ? and DNI_Dueno = ?"
            self.cursor.execute(sql, (mar, mod, mat, dni))
            rd = self.cursor.fetchall()
            if(len(rd) == 0):
                print("[ERROR] Value doesn't exist!")
                return

            if(n_action == 2):
                print("\nNuevos Datos:")
                mar, mod, mat, dni = self.get_car_data_()

                sql = "UPDATE Automoviles SET Marca = ?, Modelo = ?, Matricula = ?, \
                DNI_Dueno = ? WHERE ID = ?"
                args = (mar, mod, mat, dni, rd[0][0])
            else:
                sql = "DELETE FROM Automoviles WHERE ID = ?"
                args = (rd[0][0],)
        try:
            self.cursor.execute(sql, args)
        except sqlite3.IntegrityError:
            print("\n[ERROR] There was an error modifying database!\n")

        self.conn_bd.commit()   #commit changes
        print("\n[WARN]Database Modified!\n")

    def show_data_query_(self, n_action):
        if(n_action == 1):
            sql = "SELECT Nombre, Apellido1, Apellido2, Marca, Modelo, Matricula \
             FROM Clientes, Automoviles WHERE Clientes.DNI = Automoviles.DNI_Dueno;"
        elif(n_action == 2):
            sql = "SELECT Nombre, Apellido1, Apellido2, Empleados.DNI, Suma_Horas, Mes \
            FROM(SELECT DNI_Empleado AS'DNI', sum(Horas) AS'Suma_Horas', Mes FROM \
            Facturas GROUP BY DNI, Mes) AS'Subconsulta', Empleados \
            WHERE Empleados.DNI = Subconsulta.DNI"
        elif(n_action == 3):
            sql = "SELECT Nombre, Apellido1, Apellido2, Empleados.DNI, Media_Horas, \
            ID_Trabajo FROM(SELECT DNI_Empleado AS'DNI', avg(Horas) AS'Media_Horas', \
            ID_Trabajo FROM Facturas GROUP BY DNI, ID_Trabajo) AS'Subconsulta', Empleados \
            WHERE Empleados.DNI = Subconsulta.DNI"
        elif(n_action == 4):
            sql = "SELECT (SELECT Precio_Ud * NV FROM Repuestos WHERE Nombre = 'Ventanas'), \
            (SELECT Precio_Ud * NP FROM Repuestos WHERE Nombre = 'Puertas'), \
            (SELECT Precio_Ud * NR FROM Repuestos WHERE Nombre = 'Ruedas'), \
            (SELECT Precio_Ud * NM FROM Repuestos WHERE Nombre = 'Motores'), \
            DNI_Cliente FROM(SELECT DNI_Cliente, sum(Num_Ventanas) AS'NV', sum(Num_Puertas) \
            AS'NP', sum(Num_Ruedas) AS'NR', sum(Num_Motores) AS'NM' FROM Facturas \
            GROUP BY DNI_Cliente)"
        elif(n_action == 5):
            sql = "SELECT * FROM Facturas WHERE Cobrada = 0"

        else:
            sql = "SELECT DNI_Cliente, Nombre, Apellido1, Apellido2, Cobrada \
              FROM Facturas, Clientes \
              WHERE DNI_Cliente = Clientes.DNI and Cobrada = 0"
        return sql

    def print_table_(self):
        ret_data = self.cursor.fetchall()

        #Convert all characters to Unicode string:
        for i in range(0, len(ret_data)):
            ret_data[i] = list(ret_data[i])
            for j in range(0, len(ret_data[i])):
                if(ret_data[i][j] == None):
                    ret_data[i][j] = ""
                if(type(ret_data[i][j]) != unicode):
                    ret_data[i][j] = str(ret_data[i][j]).encode('utf-8')

        #Print line by line:
        for i in ret_data:
            print u'|'.join(i)
        #print(ret_data)

    def get_client_data_(self):
        try:
            dni = raw_input("DNI: ")
            n = raw_input("Nombre: ")
            a1 = raw_input("Primer Apellido: ")
            a2 = raw_input("Segundo Apellido: ")
            tfno = raw_input("Telefono: ")
            dir = raw_input("Direccion: ")
        except EOFError:
            sys.exit("\nQUE HACES METIENDO EOF, CEPORRO?\n")
        return dni, n, a1, a2, tfno, dir

    def get_car_data_(self):
        try:
            mar = raw_input("Marca: ")
            mod = raw_input("Modelo: ")
            mat = raw_input("Matricula: ")
            dni = raw_input("DNI Dueno: ")
        except EOFError:
            sys.exit("\nQUE HACES METIENDO EOF, CEPORRO?\n")

        return mar, mod, mat, dni

    def show_data_menu_(self):
        print("1) Listado de automoviles por clientes")
        print("2) Horas trabajadas por empleado y mes")
        print("3) Media de horas que invierte cada empleado en cada trabajo distinto")
        print("4) Consultar dinero gastado por clientes")
        print("5) Consultar las facturas pendientes")

    def show_change_client_menu_(self):
        print("1) Insertar Cliente")
        print("2) Modificar Cliente")
        print("3) Eliminar Cliente")

    def show_change_car_menu_(self):
        print("1) Insertar Automovil")
        print("2) Modificar Automovil")
        print("3) Eliminar Automovil")

def action_chosen():

    ok = True
    n = 0
    try:

        n = int(input("\nIndique una Accion: "))

    except NameError:
        ok = False
    except SyntaxError:
        ok = False
    except EOFError:
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
