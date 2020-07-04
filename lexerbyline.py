#!/usr/bin/python
from math import sqrt as rc
import os
import random

variables = {}

keywords = {
    "println!": print_builtin,
    "let": let_builtin,
    "quit": exit,
    "wipe": variables.clear

}

def print_builtin(line):
    splited = line.split(' ')
    toPrint = []
    printF = str()

    for i in range(1, len(splited) - 1):
        if i.startswith('$'):
            if i in variables.keys():
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
    
    if not (splited[2] == '=' and splited[0] == 'let'):
        print("Please use '=' to assign a value and use 'let' to declare or modify a variable")
        return

    if splited[3] == 'scan()':
            var = input("> ")
            variables[splited[1]] = var
        
    try:
        variables[splited[1]] = int(splited[3])
    except:
        variables[splited[1]] = str(splited[3])
    finally:
        print(f'Value {str(splited[3])} assigned to {splited[1]}')






def transpile(line):   

    # Comparaison de variables
    splited = line.split(' ')
                
    if line.startswith('sc'):
        print(variables[splited[1]] + variables[splited[2]])

    # Commandes système
    if splited[0] == 'sys':
        if(splited[1] == '->'):
            os.system(splited[2])
        else:
            print('Syntax Error : Try out "sys -> <command>"')

    # Exit function
    if splited[0] == 'quit':
        exit()

        
    # Wipe function
    if splited[0] == 'wipe':
        print('All variables erased !')
        variables.clear()
        
    # Opérations mathématiques
    elif splited[0] not in ['println!', 'let', 'comp', 'sqrt', 'file', 'sc', 'sys', 'quit', 'wipe']:      
        if abs(int(splited[0])) < 32768 and abs(int(splited[2])) < 32768:
            arg1 = int(splited[0])
            arg2 = int(splited[2])
            op_dict = {
                '+': lambda: arg1 + arg2,
                '-': lambda: arg1 - arg2,
                '*': lambda: arg1 * arg2,
                '/': lambda: arg1 / arg2,
                '**': lambda: arg1 ** arg2
            }
            
            if splited[1] in op_dict:
                print(op_dict[splited[1]]())
        else:
            print(f'Error, "{splited[0]}" doesn\'t exists')
