#!/usr/bin/python3

import os
import sys

ELEMENTS = []

def find_conents(base):
    contents = os.listdir(base["path"])
    for elem in contents:
        sub_base = {"name": elem, "path":os.path.join(base["path"], elem)}
        ELEMENTS.append(sub_base)
        if not os.path.isfile(sub_base["path"]):
            find_conents(sub_base)

def change_names(unis):
    for elem in unis:
        if os.path.exists(elem["path"]):
            os.rename(elem["path"], os.path.join(os.path.dirname(elem["path"]), elem["name"].encode('ascii', 'ignore').decode()))



def find_names():
    c = []
    for elem in ELEMENTS:
        try:
            elem["name"].encode('ascii')
        except:
            print("Not in ascii {0}".format(elem["name"]))
            c.append(elem)
    return c


if len(sys.argv) > 1:
    base = {"name":sys.argv[1], "path":sys.argv[1]}
    find_conents(base)
    unis = find_names()
    while unis:
        change_names(unis)
        ELEMENTS = []
        find_conents(base)
        unis = find_names()
    print("Done")
