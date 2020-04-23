#! /usr/bin/env python

import sys

class Producto():
    def __init__(self):
        self.cod = None
        self.name = None
        self.model = None
        self.price = None

class Direccion():
    def __init__(self):
        self.calle = None
        self.cod = None

class Metadata():
    def __init__(self):
        self.fecha = None
        self.dir_envio = Direccion()
        self.dir_facturacion = Direccion()
        self.cliente = None
        self.receptor = None

def set_producto(producto, comm, line):
    if(line == ""):
        return

    l = line.replace('\t', "")
    l = l.replace('\n', "")

    if(comm == "cod"):
        producto.cod = l
    elif(comm == "nombre"):
        producto.name = l
    elif(comm == "modelo"):
        producto.model = l
    elif(comm == "price"):
        producto.price = l

def set_metadata(metadatos, comm, line):
    if(line == ""):
        return

    l = line.replace('\t', "")
    l = l.replace('\n', "")

    if(comm == "fecha"):
        print(l)
        metadatos.fecha = l
    elif(comm == "envio_calle"):
        metadatos.dir_envio.calle = l
    elif(comm == "facturacion_calle"):
        metadatos.dir_facturacion.calle = l
    elif(comm == "envio_cod"):
        metadatos.dir_envio.cod = l
    elif(comm == "facturacion_cod"):
        metadatos.dir_facturacion.cod = l
    elif(comm == "cliente"):
        metadatos.cliente = l
    elif(comm == "receptor"):
        metadatos.receptor = l

def read_producto(productos, file):
    comm = ""
    producto = Producto()
    for line in file:
        if(line.find("/producto") > 0):
            break
        if(line.find("producto") > 0):
            continue
        if(line.find("/codigo") > 0):
            continue
        if(line.find("codigo") > 0):
            comm = "cod"
            continue
        if(line.find("/nombre") > 0):
            continue
        if(line.find("nombre") > 0):
            comm = "nombre"
            continue
        if(line.find("/modelo") > 0):
            continue
        if(line.find("modelo") > 0):
            comm = "modelo"
            continue

        if(line.find("/rebajado") > 0):
            continue
        if(line.find("rebajado") > 0):
            comm = "price"
            continue

        set_producto(producto, comm, line)

    productos.append(producto)

def read_metadata(metadatos, file):

    comm = ""
    envio_leido = False
    for line in file:
        if(line.find("/receptor") > 0):
            break
        if(line.find("receptor") > 0):
            comm = "receptor"
            continue
        if(line.find("/fecha") > 0):
            continue
        if(line.find("fecha") > 0):
            comm = "fecha"
            continue
        if(line.find("/envio") > 0):
            continue
        if(line.find("envio") > 0):
            envio_leido = True
            continue
        if(line.find("/calle") > 0):
            continue
        if(line.find("calle") > 0):
            if(envio_leido):
                comm = "envio_calle"
            else:
                comm = "facturacion_calle"
            continue

        if(line.find("/codigo_postal") > 0):
            continue
        if(line.find("codigo_postal") > 0):
            if(envio_leido):
                comm = "envio_cod"
                envio_leido = False
            else:
                comm = "facturacion_cod"
            continue

        if(line.find("/cliente") > 0):
            break
        if(line.find("cliente") > 0):
            comm = "cliente"
            continue

        set_metadata(metadatos, comm, line)

def read_productos(productos, metadatos, file):

    for line in file:

        if(line.find("/fecha") > 0):
            continue
        if(line.find("fecha") > 0):
            read_metadata(metadatos, file)
            continue

        if(line.find("/producto") > 0):
            break
        if(line.find("producto") > 0):
            read_producto(productos, file)

def print_head():

    print "     Matricula", "\t", "      Marca", "\t", "      Modelo"
    print(" ---------------------------------------------------")

def print_metadata(metadatos):
    print "     Fecha", "\t", "      Envio", "\t", "      Facturacion", "\t", "Cliente", "\t", "Receptor"
    print(" ---------------------------------------------------")

    print metadatos.fecha

def print_info(xml_file):

    try:
        file = open(xml_file, "r")
    except IOError:
        sys.exit("Error Openning File!")

    productos = []
    metadatos = Metadata()
    read_productos(productos, metadatos, file)

    print_metadata(metadatos)
    '''
    print_head()

    for i in productos:
        print i.cod, "\t" , i.name, "\t", i.model, "\t", i.price
    '''
    file.close()

if __name__ == "__main__":

    xml_file = "ejercicio1.xml"

    print_info(xml_file)

    exit(0)
