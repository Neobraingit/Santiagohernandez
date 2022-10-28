# ¿Qué es un diccionario?
'''Corresponden con una clave-valor y van entre llaves'''
dic = {
    'Nombre': 'Marcos',
    'Apellidos': 'Carmona',
    'Edad' : 48}
print (type(dic))


# Acceso a los elementos de un diccionario
''' Se accede a los elementos utilizando el nombre de la clave y no se usa slicing'''
print (dic['Nombre'])
print (dic['Edad'])
'''No respetan el orden y sus valores pueden ser modificados y podemos añadir un nuevo elemento cuando queramos.
Podemos añadir cualquier tipo de dato.'''
dic ['Ciudad'] = 'Gijon'
print (dic)

'''No puede haber dos claves con el mismo nombre'''

# Operaciones con diccionarios
dic3 = {'key1' : 'value1', 'key2' : 'value2'}
dic4 = {'key3' : 'value3', 'key4' : 'value4'}
'''No podemos concatenar dos diccionarios'''

