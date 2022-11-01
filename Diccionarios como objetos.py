dic = {
    'Nombre' : 'Marcos',
    'Apodo' : 'Cuca'
}
dic2 = {}

# Modificando un diccionario
dic.update({'Nombre' : 'Alberto'}) # Actualizamos una clave del diccionario
print (dic)
dic.pop('Nombre') # Nos muestra el valor de una clave pasada y lo borra
print (dic)
dic2 = dic.copy() # Nos copia el diccionario en otro
print (dic2)
dic.clear() # Elimina y vacía el diccionario
print (dic)

# Accediendo a los elementos
dic3 = {
    'Nombre' : 'Marcos',
    'Apellido' : 'Carmona',
    '2º Apellido' : 'García'
}

print (dic3.values()) # Nos devuelve todos los valores en formato lista
print (dic3.keys()) # Nos devuelve todas las claves
print (dic3.items()) # Nos devuelve el contenido en formato tupla y nos permite recorrerlo con un bucle for
for key, value in dic3.items():
    print (key)
    print (value)
