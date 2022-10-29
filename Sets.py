# ¿Qué son los sets en Python?
'''Permiten almacenar múltiples elementos en una variable, pero no se pueden indexar, no respetan un orden
y no puede contener valores duplicados. Se representan con llaves'''
set = {'val1', 'val2', 'val3'}
print (set)

# La mayor utilidad de los sets es eliminar valores dupolicado de listas
lista = ['rojo', 'rojo', 'verde', 'verde']

# Frozenset
'''Es exactamente igual al set solo que es inmutable'''
fset = frozenset({'azul', 'verde'})
print (type(fset))
