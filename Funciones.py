# ¿Qué es una función?
# Es un bloque de código que encapsula una porción de código que hará algo y será reutilizable
var = 'Hola mundo'
print (len(var)) # Esta función (len) predefinida nos devuelve la longitud de la variable

# Definiendo funciones personalizadas
def mi_funcion(): #def + nombrefunción + parámetros
    print ('Hola mundo')

mi_funcion() # Invocamos nuestra función para que se ejecute

def mi_funcion2(arg1, arg2): # Otra función con parámetros
    print (arg1)
    print (arg2)

mi_funcion2('Marcos', 'Carmona') # Invocamos la función con los parámetros requeridos

# Los argumentos de las funciones pueden ser de distinto tipo
# Argumentos posicionales: son separados por comas y son los más sencillos de crear y tienen que tener el número declarado y el orden
# Argumentos de palabra clave: son los que tienen palabra_clave + valor
def mi_funcion3(arg1, arg2):
    print (arg1)
    print (arg2)
var = 123
var2 = 'Marcos'
mi_funcion3(arg1 = var, arg2 = var2) # Con esto no tenemos que respetar el orden de los parámetros aunque hay que seguir respetando el número de parámetros

# Parámetros con valores por defecto u opcionales: el valor se convierte en el valor por defecto del parámetro
def mi_funcion4(arg1, arg2 = 'valor por defecto'):
    print (arg1)
    print (arg2)

mi_funcion4('Hola mundo', 'Adios mundo')

#Sentencia Return
# Las funciones en Python pueden retornar un valor después de haber ejecutado las sentencias de código definidas. Para hacer esto se utiliza return
def mi_funcion5():
    print ('sentencia 1 dentro de la función')
    return
    print ('sentencia 2 dentro de la función')
print ('sentencia 1 fuera de la función')
mi_funcion5()
print ('sentencia 2 fuera de la función')

def mifuncion6():
    return 'Retorno del return'
var = mifuncion6()
print (var)

mifuncion6()[0:2] # Hacemos un slicing cogiendo como string el valor del return
# Si no indicamos ningún valor al return nos devolverá None
def mifuncion7():
    return
var3 = mifuncion7()
print (var3)

# Podemos asignar múltiples valores a variables usando return
def mifuncion8():
    return 'asig1', 'asig2', 'asig3'
var3,var4,var5 = mifuncion8()
print (var3)
print (var4)
print (var5)

# Docstrings: nos sirve para documentar las funciones
def mifuncion9():
    '''Esta función nos muestra por pantalla un string'''
    print ('Hola Marcos')

mifuncion9()

# Funciones propias de Python
# https://docs.python.org/3/library/funtions.html
help(print) # Nos muestra la documentación de un objeto que le pasemos
print() # Nos imprime por pantalla lo que le pongamos
str(), int(), float() # Nos sirve para hacer casting de objetos
type(print) # Nos muestra el tipo de un objeto
id(var3) # Nos retorna la identidad de un objeto, siendo esta única entre los demás objetos
var7 = "print ('Esto es un ejemplo de exec')"
exec(var7) # Ejecuta el código que está representado como string







