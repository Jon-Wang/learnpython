#!/usr/bin/python
#filename:func_doc.py

def printMax(x,y):
    '''Print the maximum of two numbers.
    
    The two value must be integers.'''
    x=int(x)#convert to integers,if possible
    y=int(y)

    if x>y:
        print x,'is maximum'
    else:
        print x,'is maximum'

printMax(3,5)
print printMax.__doc__
