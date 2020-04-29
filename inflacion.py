#! /usr/bin/env python

import json
import sys

#CONSTS:
Inflacion = 3

if __name__ == '__main__':

    try:
        file = open("papeleria.json", "r")
    except IOError:
        sys.exit("[ERROR] Problem openning file\n")

    data = json.load(file)

    for i in data:
        claves = i.keys()
        i[claves[2]]=i[claves[2]]*(1 + Inflacion * 0.01)
        print json.dumps(i)

    file.close()
    exit(0)
