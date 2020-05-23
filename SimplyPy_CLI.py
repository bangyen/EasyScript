#!/usr/bin/python
from math import sqrt as rc

# This is the CLI version of SimplyPy
# The instructions available are : 
# println! { <string> and println! # <variable> DONE
# Mathematicals operations :  '+' '-' '/' '*' 'sqrt' TODO
# Variables declaration : let <name> <value> DONE

variables = dict()

def saisie():
    saisie = input('>>> $ ')
    splited = saisie.split(' ', 2)


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

    if(splited[0] == 'let'):
        variables[splited[1]] = splited[2]
        if(splited[2] != ''):
            print('Val \'' + str(splited[2]) + '\' assigned to ' + str(splited[1]))
        elif(splited[2] == ''):
            print('Variable \'' + str(splited[1] + '\' initialized'))

    if(splited[0] == 'help'):
        print("To display a string : println! { <text>\nTo display a variable : println! # <var>\nTo initialize a variable : let <var> (don't forget the space)\nTo modify a variable value : let <var> <value>\nTo concatenate two String variables : <str_a> + <str_b>")
    


    elif(splited[0] != 'println!' and splited[0] != 'let' and splited[0] != 'help' and splited[0] != 'sq['):
        if(splited[0] in variables.keys() and splited[2] in variables.keys()):
            if(splited[1] == '+'):
                print(variables[splited[0]] + variables[splited[2]])
        try:
            arg1 = int(splited[0])
            arg2 = int(splited[0])
        except:
            print('Error, "' + splited[0] + '" doesn\'t exists')
        else:
            print('Error, "' + splited[0] + '" doesn\'t exists')

while True:
    saisie()