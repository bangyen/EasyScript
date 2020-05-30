#!/usr/bin/python

from lexerbyline import transpile

def parse(liste):
    for i in range(0, len(liste - 1)):
        transpile(liste[i])

def con():
    content = []
    txt = input('...')
    i = 0

    while(txt != '}'):
        content[i] = txt
        i += 1
        txt = input('...')
    parse(content)    