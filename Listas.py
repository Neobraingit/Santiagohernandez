# ¿Qué son las listas?
''' Van entre corchetes y se definen como list y pueden tener cualquier tipo de objeto e incluso funciones y son mutables'''
lista = [1, 2, 3, 4, 5]
print (type(lista))
print (lista)

lista2 = ['Nombre', 'Apellido', 'Edad']
print (lista2)

# Podemos utilizar todos los operadores con las listas
print ('Nombre' in lista2)

# Pueden contener funciones
def mifuncion():
    print ('Hola mundo')

lista3 = [mifuncion(), '2']
print (lista3)

# Acceso a los elementos de una lista (indexing)
lista4 = ['Nombre', 3, 'Carmona', 'García', 123]
print (lista4[0])
# Slicing
print (lista4[0:3])
# Stride
print (lista4[0:3:1])
print (lista4[::-1]) # Con esto le damos la vuelta a la lista


# Operaciones con listas
lista5 = [1,2,3,4]
lista6 = [5,6,7,8]
print (lista5 + lista6) # Como vemos las listas sumadas se concatenan
print (lista5 * 2)
print (len(lista5))
print (min(lista5)) # Nos devuelve el elemento menos de la lista
print (max(lista5)) # Nos devuelve el elemento mayor de la lista

# Anidado de listas
lista7 = [1,2,3,4,[lista5]]
print (lista7)

# Las listas son mutables
lista8 = [ 'Marcos', 'texto1', 'texto2', 'texto3']
lista8[0] = 'García'
print (lista8)

# También podemos eliminar un elemento de una lista
del(lista8[0])
print (lista8)





