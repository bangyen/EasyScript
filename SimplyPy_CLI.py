#!/usr/bin/python
from math import sqrt as rc

# This is the CLI version of SimplyPy
# The instructions available are : 
# println! { <string> and println! # <variable> DONE
# Mathematicals operations :  '+' '-' '/' '*' 'sqrt' DONE
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
    
    if(splited[0] == 'sqrt'):
        try:
            nombre = int(splited[1])
            print(rc(nombre))
        except:
            print('You cannot calculate the square root of a string litteral !')
    if(splited[0] == 'sc'):
        print(variables[splited[1]] + variables[splited[2]])
        

    elif(splited[0] != 'println!' and splited[0] != 'let' and splited[0] != 'help' and splited[0] != 'sqrt' and splited[0] != 'sc'):      
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
                for i in range(1, arg2 + 1):
                    arg1 *= origin
                print(arg1)
        else:
            print('Error, "' + splited[0] + '" doesn\'t exists')

while True:
    saisie()