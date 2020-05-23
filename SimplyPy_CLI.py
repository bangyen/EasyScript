#!/usr/bin/python

# This is the CLI version of SimplyPy
# The instructions available are : 
# println! {<string> and println! #<variable>
# Mathematicals operations :  '+' '-' '/' '*' 'sqrt'
# Variables declaration : let <name> <value>

variables = dict()

def saisie():
    saisie = input('>>> $ ')
    splited = saisie.split(' ')

    # Functionnal

    if(splited[0] == 'println!'):
        if(splited[1].startswith('{')):
            instruct = splited[1]
            toShow = instruct[1:]
            print(toShow)

    # TO TEST
    if(splited[0] == 'let'):
        variables[splited[1]] = splited[2]
        print('Val ' + str(splited[2] + ' assigned to ' + str(splited[1])))
    
        
    else:
        print('Error, "' + splited[0] + '" doesn\'t exists')

while True:
    saisie()