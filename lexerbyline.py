#!/usr/bin/python
from math import sqrt as rc
import os
import random

variables = {}

keywords = {
    "println!": print_builtin,
    "let": let_builtin
}

def print_builtin(line):
    splited = line.split(' ')
    toPrint = []
    printF = str()

    for i in range(1, len(splited) - 1 ):
        if(i.startswith('$')):
            if(i in variables.keys()):
                toPrint.append(str(variables[i]))
            else:
                print("No variable named " + i[1:])
        else:
            toPrint.append(str(i))
            
    for e in toPrint:
        printF += e

    print(printF)

def let_builtin (line):
    splited = line.split(' ', 4)
    
    if not(splited[2] == '=' and splited[0] == 'let'):
        print("Please use '=' to assign a value and use 'let' to declare or modify a variable")
        return
    try:
        variables[splited[1]] = int(splited[3])
    except:
        variables[splited[1]] = str(splited[3])
    finally:
        print(f'Value {str(splited[3])} assigned to {splited[1]}')





def transpile(line):   

    # Variables
    if(line.startswith('let')):

        splited = parse(3, ' ', line)
        
        # Input
        if(splited[2] == 'scan()'):
            var = input("> ")
            variables[splited[1]] = var
        
        # Random
        if(splited[2].startswith('rand()')):
            splitIn = splited[2].split(' ')
            if(splitIn[2] == '->'):
                try:
                    a = int(splitIn[1])
                    b = int(splitIn[3])
                    fin = random.randint(a, b)
                    variables[splited[1]] = fin
                except:
                    print('Please specify two integers')
            else:
                print('Syntax Error : Did you mean "let <var> rand() <number> -> <number>" ?')

        elif(splited[2] != '' and splited[2] != 'scan()'):
            variables[splited[1]] = splited[2]
            print('Val \'' + str(splited[2]) + '\' assigned to ' + str(splited[1]))

        elif(splited[2] == ''):
            variables[splited[1]] = splited[2]
            print('Variable \'' + str(splited[1] + '\' initialized'))



    # Comparaison de variables
    if(line.startswith('comp')):
        splited = parse(1, ' ', line)
        if((splited[1]) in variables.keys() and splited[2] in variables.keys()):
            if(variables[splited[1]] == variables[splited[2]]):
                print(splited[1] + '==' + splited[2])
            if(variables[splited[1]] != variables[splited[2]]):
                print(splited[1] + '!=' + splited[2])
                
    # Calcul de racine carrée
    if(line.startswith('sqrt')):
        splited = parse(1, ' ', line)
        try:
            nombre = int(splited[1])
            print(rc(nombre))
        except:
            print('You cannot calculate the square root of a string litteral !')
    if(line.startswith('sc')):
        print(variables[splited[1]] + variables[splited[2]])

    # Commandes système
    if(splited[0] == 'sys'):
        if(splited[1] == '->'):
            os.system(splited[2])
        else:
            print('Syntax Error : Try out "sys -> <command>"')

    # Exit function
    if(splited[0] == 'quit'):
        exit()

        
    # Wipe function
    if(splited[0] == 'wipe'):
        print('All variables erased !')
        variables.clear()
        
    # Opérations mathématiques
    elif(splited[0] != 'println!' and splited[0] != 'let' and splited[0] != 'comp' and splited[0] != 'sqrt' and splited[0] != 'file' and splited[0] != 'sc' and splited[0] != 'sys' and splited[0] != 'quit' and splited[0] != 'wipe'):      
        if(int(splited[0]) > -32768 and int(splited[0]) < 32768 and int(splited[2]) > -32768 and int(splited[2]) < 32768):
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