#! /usr/bin/env python
import datetime
import pytz
import sys
import optparse
import datetime

#CONSTS
TimestampFields = 2
FullDateFields = 4
AllowedCities = ["Madrid", "Londres", "Moscu", "Tokio", "New_York", "UTC"]

def is_integer(str):

    for i in range(0, len(str)):
        try:
            n = int(i)
        except ValueError:
            return False

    return True

def is_date(str):
    text_arr = str.split('-')
    for i in text_arr:
        if(not is_integer(i)):
            return False

    return True

def is_hour(str):
    s = str.replace(',', "")
    text_arr = s.split(':')

    for i in text_arr:
        if(not is_integer(i)):
            return False

    return True

def is_str_allowed(str):
    s = str.replace('\n', "")

    return s in AllowedCities

def is_timestamp(line):
    text_arr = line.split(' ')

    if(len(text_arr) != TimestampFields):
        return False

    return is_integer(text_arr[TimestampFields - 2]) and is_integer(text_arr[TimestampFields - 1])

    return True

def is_full_date(line):

    text_arr = line.split(' ')

    if(len(text_arr) != FullDateFields):
        return False

    return is_integer(text_arr[FullDateFields - 4]) and is_date(text_arr[FullDateFields - 3]) and \
            is_hour(text_arr[FullDateFields - 2]) and is_str_allowed(text_arr[FullDateFields - 1])

def line_ok(line):

    return is_full_date(line) or is_timestamp(line)

def file_ok(file):
    eof = False
    ok = True
    while(not eof):
        line = file.readline()
        eof = line == ''
        if(not eof):
            if(not line_ok(line)):
                ok = False
                break;
    return ok

def add_parser_options(parser):

    options_list = ["-t", "--timezone"]
    for i in range(0, len(options_list), 2):
        parser.add_option(options_list[i], options_list[i + 1], action="store_true")

def ts2utc(line):
    t_arr = line.split(' ')
    dt = datetime.datetime.utcfromtimestamp(float(t_arr[TimestampFields - 1]))

    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    t_arr[TimestampFields - 1] = dt.strftime(fmt)

    return ' '.join(t_arr)

def full_date2utc(line):
    l = line.replace(',', "")
    t_arr = l.split(' ')
    l = t_arr[FullDateFields - 3:FullDateFields - 1]

    dt = datetime.datetime.strptime(' '.join(l), "%Y-%m-%d %H:%M:%S")
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    l[0] = t_arr[0]
    l[1] = dt.strftime(fmt)

    return ' '.join(l)

def print_times(file, options, args):
    eof = False
    while(not eof):
        line = file.readline()
        eof = line == ''
        if(eof):
            continue

        if(len(args) == 0 or options.timezone == "utc"):
            if(is_timestamp(line)):
                print(ts2utc(line))
            if(is_full_date(line)):
                print(full_date2utc(line))



if __name__ == "__main__":

    #Open file
    try:
        file = open("fechas.txt", "r")
    except IOError:
        sys.exit("[ERROR] Problem openning file\n")

    if(not file_ok(file)):
        sys.exit("[ERROR] File format is not allowed\n")
    file.close()

    parser = optparse.OptionParser("Usage: %prog [options] arg")
    add_parser_options(parser)

    (options, args) = parser.parse_args()

    #print(options.timezone)
    #print(args)
    file = open("fechas.txt", "r")
    print_times(file, options, args)

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
    exit(0)
