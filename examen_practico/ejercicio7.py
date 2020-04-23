#! /usr/bin/env python

import requests as reqs
import sys

def print_country(ip):
    url = "https://api.ip2country.info/ip?"
    query = url + ip

    reply = reqs.get(query)
    if(reply.status_code != 200):
        sys.exit("[ERROR] Can't acces to page")

    reply = reply.json()

    if(reply['countryName'] == ''):
        print("\nNo se corresponde con ningun pais\n")
        return

    print(reply['countryName'])

if __name__ == "__main__":

    if(len(sys.argv) < 2):
        sys.exit("Usage error!")

    ip = sys.argv[1]
    print_country(ip)

    exit(0)
