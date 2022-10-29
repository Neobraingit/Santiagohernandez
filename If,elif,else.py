# ¿Qué son las estructuras de control de flujo?
'''Nos permiten cambiar el control de ejecución de un programa'''

# Sentencia if
'''Esta estructura nos permite implementar sentencias condicionales dentro de nuestro programa
. La sintaxis es así:
  if expresión:
      sentencia'''
num1 = 12
num2 = 10
if num1 < num2:
    print ('Hola mundo')
elif num1 > num2:
    print ('Adios mundo')

lista = ['Azul', 'verde', 'violeta']

if 'Azul' in lista:  # Podemos usar el if con cualquier tipo de dato. En este caso con una tupla
    print ('Efectivamente; está')
else:
    print ('No está')
