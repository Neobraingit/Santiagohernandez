def relu (x):
    '''Calcula el resultado de la función matemática Relu'''
    return max(0, x)

from math import e

def sigmoid (x):
    '''Calcula el resultado de la función matemática Sigmoid'''
    resultado = 1 / (1 + e ** -x)
    return resultado

from math import e

def sinh (x):
    '''Esto calcula el resultado matemático de la función Sinh'''
    return (e ** x - e ** -x) / 2

def cosh (x):
    '''Calcula el resultado matemático de la función Cosh'''
    return (e ** x + e ** -x) / 2

def tanh (x):
    '''Esta función calcula el resultado matemático de la Tanh'''
    return sinh(x) / cosh(x)

print (tanh(0))
print (tanh(100))