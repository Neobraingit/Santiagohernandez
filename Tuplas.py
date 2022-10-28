# ¿Qué son las tuplas?
'''Son como las listas, pero van entre paréntesis y son inmutables'''
tupla = (1,2,3,4,5,6)
print (tupla)

# Funcionamiento de las tuplas
'''Se pueden mezclar distintos tipos de datos'''
tupla2 = (1,2,3,'Marcos', 'Carmona')
print (tupla2)

# Slicing
print (tupla2[2])

# Cuando utilizar una tupla en vez de una lista
'''-La ejecución del programa es más rápida
   -Para proteger cambios en los elementos de la tupla
   '''

# Tuplas y tipos de datos numéricos
'''Hay que tener cuidado con los paréntesis de la tupla por que Python puede
interpretarlos como parte de una operación matemática. Para solucionar esto
se pone una coma después de la tupla (5,)'''

# Packing y Unpacking
tupla3 = (1,2,3,4,5,6)
num1, num2, num3, num4, num5, num6 = tupla3 # Asignamos los valores de la tupla a variables simultáneamente
print (num1)

