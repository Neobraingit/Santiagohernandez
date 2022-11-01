lista = ['Marcos', 'Carmona', 'García']

# Modificando una lista
print (lista)
lista.append('cuca') # Añade un valor a la lista
print (lista)
lista.extend(['Eva', 'Alonso'])  # Para añadir varios elementos hay que pasarlos como lista
print (lista)
lista.remove('cuca') # Borra lo que le digamos
print (lista)
lista.reverse() # Le da la vuelta a la lista
print (lista)
lista.pop() # Saca el último elemento de la lista y lo borra
print (lista)
lista2 = lista.copy() # Copia la lista en otra
print (lista2)
lista.clear() # Te deja la lista vacía
print (lista)

# Acceder a elementos de la lista
lista = ['verde', 'rojo']
print (lista.index(('verde'))) # Nos muestra el índice de un elemento
print (lista.count('verde')) # Nos muestra elementos duplicados