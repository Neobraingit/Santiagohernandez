# ¿Qué son las excepciones?
'''Python utiliza un tipo de objeto especial denominado excepción para gestionar los errores que surgen durante la ejecución de un programa'''


try:
    print (var)
except NameError:
    var = 'Hola mundo' # Esto dice que si no ejecuta lo de try, lo modifica
print (var)

# Aquí vemos un ejemplo
try:
    print ('Código antes de la excepción')
    10 + '3'
    print ('Código después de la excepción')
except TypeError:
    print ('No se puede sumar un número y un string')


# Podemo usar escept sin añadir ninguna excepción
try:
    10 + '3'
except:
    print ('No tiene excepción')

# Podemos capturar varias excepciones con múltiples except
try:
    print (variable)
except NameError:
    print ('Gestionando excepción Namerror')
except TypeError:
    print ('Gestionando excepción Typerror')

# Lanzando excepciones personalizadas
colores = ('amarillo', 'rojo', 'verde')
color = 'azul'
if color not in colores:
    raise Exception('Ese color no está permitido...'.format(color))




