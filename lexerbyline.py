#!/usr/bin/python
from math import sqrt as rc
import os
import random

variables = dict()


def transpile(line):
    splited = line.split(' ', 2)

    

    # Affichage
    if splited[0] == 'println!':
        if splited[1] == 'str':
            toShow = splited[2]
            print(toShow)
        elif splited[1] == 'var':
            instruct = splited[2]
            if instruct in variables.keys():
                print(variables[instruct])
            else:
                print('No variable named "' + splited[2] + '"')

    # Variables
    elif splited[0] == 'let':
        
        # Input
        if splited[2] == 'scan()':
            var = input("> ")
            variables[splited[1]] = var
        
        # Random
        elif splited[2].startswith('rand()'):
            splitIn = splited[2].split(' ')
            if splitIn[2] == '->':
                try:
                    a = int(splitIn[1])
                    b = int(splitIn[3])
                    fin = random.randint(a, b)
                    variables[splited[1]] = fin
                except:
                    print('Please specify two integers')
            else:
                print('Syntax Error : Did you mean "let <var> rand() <number> -> <number>" ?')

        else:
            variables[splited[1]] = splited[2]
            if splited[2] != '':
                print('Val \'' + str(splited[2]) + '\' assigned to ' + str(splited[1]))
            else:
                print('Variable \'' + str(splited[1] + '\' initialized'))

    # Comparaison de variables
    elif splited[0] == 'comp':
        if splited[1] in variables.keys() and splited[2] in variables.keys():
            if variables[splited[1]] == variables[splited[2]]:
                print(splited[1] + '==' + splited[2])
            else:
                print(splited[1] + '!=' + splited[2])
                
    # Calcul de racine carrée
    elif splited[0] == 'sqrt':
        try:
            nombre = int(splited[1])
            print(rc(nombre))
        except:
            print('You cannot calculate the square root of a string litteral !')

    elif splited[0] == 'sc':
        print(variables[splited[1]] + variables[splited[2]])

    # Commandes système
    elif splited[0] == 'sys':
        if splited[1] == '->':
            os.system(splited[2])
        else:
            print('Syntax Error : Try out "sys -> <command>"')

    # Exit function
    elif splited[0] == 'quit':
        exit()
        
    # Wipe function
    elif splited[0] == 'wipe':
        print('All variables erased !')
        variables.clear()
        
    # Opérations mathématiques
    elif != 'file':
        if -32768 < int(splited[0]) < 32768 and -32768 < int(splited[2]) < 32768:
            arg1 = int(splited[0])
            arg2 = int(splited[2])
            res_dict = {
                '+': arg1 + arg2,
                '-': arg1 - arg2,
                '*': arg1 * arg2,
                '/': arg1 / arg2
            }

            if splited[1] in res_dict:
                print(res_dict[splited[1]])
            if splited[1] == '**':
                origin = arg1
                for i in range(1, arg2):
                    arg1 *= origin
                print(arg1)
        else:
            print('Error, "' + splited[0] + '" doesn\'t exists')
