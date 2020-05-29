#Task 4&5: Hello <name> using command line
# and it works with multiple arguments

import sys


def hello(name):
    if name == None or name == "":
        return 'Hello, World!'
    else: 
        return 'Hello,' + name + '!'
    
lista = (sys.argv)

text= ""

for nume in lista[1:]:
    text += " " + nume
    
print(hello(text))