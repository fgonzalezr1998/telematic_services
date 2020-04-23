#! /usr/bin/env python

import sys
import json
import requests as reqs



if __name__ == "__main__":


    url = "https://datos.madrid.es/egob/catalogo/200342-0-centros-dia.json"

    reply = reqs.get(url)
    if(reply.status_code != 200):
        sys.exit("[ERROR] Can't acces to page")

    reply = reply.json()

    exit(0)
