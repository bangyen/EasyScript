from lexerbyline import transpile

#!/usr/bin/python
from math import sqrt as rc
import os
import random

variables = dict()

def execute():
    path = input('Write file path >>> $ ')
    fichier = open(path, 'r')
    f = fichier.read()
    sliced = f.split('\n')

    length = len(sliced) - 1

    for i in range(0, length):
        transpile(sliced[i])

while True:
    execute()
