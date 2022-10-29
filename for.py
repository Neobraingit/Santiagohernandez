# ¿Qué es la sentencia for?
'''Esta sentencia nos permite repetir sentencias un número finito de veces'''
nombre = 'Marcos Carmona García'
for i in nombre: # Iteramos toda la cadena de texto y la sacamos por pantalla
    print (i)

colores = ['azul', 'rojo', 'verde']
for i in colores:
    print (i)

# Para saber si un elemento es iterable
print (iter('cadena de texto'))
print (iter([1,2,3,4]))

# Cláusula else en un bucle for. Se ejecutará cuando ya no haya nada que iterar
lista = ['azul', 'verde', 'amarillo']
for i in lista:
    print (i)
else:
    print ('El bucle ya no tiene elementos...')

# Range
for i in range(0,100, 5): # Vamos del cero al cien de cinco en cinco
    print (i)
