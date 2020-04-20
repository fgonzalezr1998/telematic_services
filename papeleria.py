#! /usr/bin/env python

import json
import sys
import os

#CONSTS:
JsonFile = "papeleria.json"

def print_header():
    print "Ref." + "\t  Precio" + "\tDescripcion"
    print("------------------------------------")

def print_info(file):
    try:
        data = json.load(file)
    except ValueError:
        sys.exit("[ERROR] JSON Format is not correct!")

    for i in data:
        print str(i['ref']) + "\t  " + str(i['precio']) + "\t    " + i['descripcion']

if __name__ == "__main__":
    #OPen JSON file:
    try:
        file = open(JsonFile, "r")
    except IOError:
        sys.exit("[ERROR] Problem openning Json file!")

    print_header()
    print_info(file)

    file.close()

    exit(0)
