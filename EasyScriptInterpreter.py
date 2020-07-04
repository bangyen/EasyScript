#!/usr/bin/python

from lexerbyline import transpile
from math import sqrt as rc
import os
import random

variables = dict()

def execute():
    path = input('Write file path >>> $ ')
    fichier = open(path, 'r')
    f = fichier.read()
    sliced = f.split('\n')

    length = len(sliced)

    for i in range(length):
        transpile(sliced[i])

while True:
    execute()
