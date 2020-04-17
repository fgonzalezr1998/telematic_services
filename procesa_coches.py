#! /usr/bin/env python

import sys

class Coche():
    def __init__(self):
        self.matricula = None
        self.marca = None
        self.model = None

def set_param(coches, coche, comm, line):
    if(line == ""):
        return

    l = line.replace('\t', "")
    l = l.replace('\n', "")

    if(comm == "matricula"):
        coche.matricula = l
    elif(comm == "marca"):
        coche.marca = l
    elif(comm == "modelo"):
        coche.modelo = l

def read_coche(coches, file):
    comm = ""
    coche = Coche()
    for line in file:
        if(line.find("/coche") > 0):
            break
        if(line.find("coche") > 0):
            continue
        if(line.find("/matricula") > 0):
            continue
        if(line.find("matricula") > 0):
            comm = "matricula"
            continue
        if(line.find("/marca") > 0):
            continue
        if(line.find("marca") > 0):
            comm = "marca"
            continue
        if(line.find("/modelo") > 0):
            continue
        if(line.find("modelo") > 0):
            comm = "modelo"
            continue
        set_param(coches, coche, comm, line)

    coches.append(coche)


def read_coches(coches, file):

    for line in file:
        if(line.find("/coche") > 0):
            break
        if(line.find("coche") > 0):
            read_coche(coches, file)

def print_head():

    print "     Matricula", "\t", "      Marca", "\t", "      Modelo"
    print(" ---------------------------------------------------")

def print_info(xml_file):

    try:
        file = open(xml_file, "r")
    except IOError:
        sys.exit("Error Openning File!")


    coches = []
    read_coches(coches, file)

    print_head()

    for i in coches:
        print i.matricula, "\t" , i.marca, "\t", i.modelo

    file.close()

if __name__ == "__main__":

    xml_file = "coches.xml"

    print_info(xml_file)
