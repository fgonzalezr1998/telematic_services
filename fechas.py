#! /usr/bin/env python
import datetime
import pytz
import sys

if __name__ == "__main__":

    #Open file
    try:
        file = open("fechas.txt", "r")
    except IOError:
        sys.exit("[ERROR] Problem openning file\n")

    if(not file_ok(file)):
        sys.exit("[ERROR] File format is not allowed\n")

    '''
    eof = False
    while(not eof):
        line = file.readline()
        eof = line == ''
        if(not eof):
            print(line)
        i = i + 1
    '''

    file.close()
