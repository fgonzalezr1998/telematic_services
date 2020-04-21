#! /usr/bin/env python

import requests as reqs
import sys
import optparse
import json

def print_data(u, c):
    print "De: ", u["username"]
    print c["title"]
    print "---------------------------------"
    print c["body"], "\n"

def exists(username, users_list):
    for i in users_list:
        if(username.lower() == i['username'].lower()):
            return True
    return False

def args_ok(options, args, user_list):
    ok = True
    if(options.user):
        if(len(args) > 0):
            if(exists(args[0], user_list)):
                ok = True
            else:
                print("[ERROR] Username doesn't exist!")
                ok = False
        else:
            ok = False
    return ok

def print_requests(options, args):
    #Get to both resources
    content = reqs.get("http://jsonplaceholder.typicode.com/posts")
    if(content.status_code != 200):
        sys.exit("[ERROR] Can't access to page content")
    user = reqs.get("http://jsonplaceholder.typicode.com/users")
    if(user.status_code != 200):
        sys.exit("[ERROR] Can't access to page users")

    content = content.json()
    user = user.json()
    print(args)
    print(options.user)
    if(not args_ok(options, args, user)):
        sys.exit("[ERROR] Invalid Arguments!")

    for i in user:
        for j in content:
            if(j['userId'] == i['id']):
                if(options.user):
                    if args[0].lower() == i["username"].lower():
                        print_data(i, j)
                else:
                    print_data(i, j)

def add_parser_options(parser):

    options_list = ["-u", "--user"]
    for i in range(0, len(options_list), 2):
        parser.add_option(options_list[i], options_list[i + 1], action="store_true")


if __name__ == "__main__":
    #Add parameters to argparse
    parser = optparse.OptionParser("Usage: %prog [options] arg")
    add_parser_options(parser)

    (options, args) = parser.parse_args()

    print_requests(options, args)

    exit(0)
