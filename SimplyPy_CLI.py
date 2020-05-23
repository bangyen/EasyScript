#!/usr/bin/python

# This is the CLI version of SimplyPy
# The instructions available are : 
# println! {<string> ; and println! #<variable> ;
# Mathematicals operations :  '+' '-' '/' '*' 'sqrt'
# Variables declaration : let <name> <value> ;

def saisie():
    saisie = input('>>> $ ')
    splited = saisie.split(' ')

    if(splited[0] == 'println!'):
        if(splited[1].startswith('{')):
            instruct = splited[1]
            toShow = instruct[1:]
            print(toShow)
    else:
        print('Error,' + splited[0] + ' doesn\'t exists')
saisie()