#!/usr/bin/python
from math import sqrt as rc
import os

variables = dict()

def saisie():
    saisie = input('>>> $ ')
    splited = saisie.split(' ', 2)

    # Affichage
    if(splited[0] == 'println!'):
        if(splited[1] == '{'):
            toShow = splited[2]
            print(toShow)
        if(splited[1] == '#'):
            instruct =  splited[2]
            if(instruct in variables.keys()):
                print(variables[instruct])
            else:
                print('No variable named "' + splited[2] + '"')

    # Variables
    if(splited[0] == 'let'):
        variables[splited[1]] = splited[2]
        if(splited[2] != ''):
            print('Val \'' + str(splited[2]) + '\' assigned to ' + str(splited[1]))
        elif(splited[2] == ''):
            print('Variable \'' + str(splited[1] + '\' initialized'))

    # Comparaison de variables
    if(splited[0] == 'comp'):
        if((splited[1]) in variables.keys() and splited[2] in variables.keys()):
            if(variables[splited[1]] == variables[splited[2]]):
                print(splited[1] + '==' + splited[2])
            if(variables[splited[1]] != variables[splited[2]]):
                print(splited[1] + '!=' + splited[2])
                
    # Calcul de racine carrée
    if(splited[0] == 'sqrt'):
        try:
            nombre = int(splited[1])
            print(rc(nombre))
        except:
            print('You cannot calculate the square root of a string litteral !')
    if(splited[0] == 'sc'):
        print(variables[splited[1]] + variables[splited[2]])

    # Commandes système
    if(splited[0] == 'sys'):
        if(splited[1] == '->'):
            os.system(splited[2])
        else:
            print('Syntax Error : Try out "sys -> <command>"')
        
    # Opérations mathématiques
    elif(splited[0] != 'println!' and splited[0] != 'let' and splited[0] != 'comp' and splited[0] != 'sqrt' and splited[0] != 'sc' and splited[0] != 'sys'):      
        if(int(splited[0]) > -255 and int(splited[0]) < 255 and int(splited[2]) > -255 and int(splited[2]) < 255):
            arg1 = int(splited[0])
            arg2 = int(splited[2])

            if(splited[1] == '+'):
                print(arg1 + arg2)
            if(splited[1] == '-'):
                print(arg1 - arg2)
            if(splited[1] == '*'):
                print(arg1 * arg2)
            if(splited[1] == '/'):
                print(arg1 / arg2)
            if(splited[1] == '**'):
                origin = arg1
                for i in range(1, arg2):
                    arg1 *= origin
                print(arg1)
        else:
            print('Error, "' + splited[0] + '" doesn\'t exists')

while True:
    saisie()