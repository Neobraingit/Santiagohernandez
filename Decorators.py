# Conceptos avanzados sobre funciones
'''Un decorator es algo que envuelve una función modificando su compartamiento'''

def mi_funcion():
    print ('Hola mundo¡¡')

def mi_decorator (mi_funcion):
    def wrapper():
        print ('Ejecución antes de la llamada a la función')
        mi_funcion()
        print ('Ejecución después de la función')
    return  wrapper()

mi_funcion_modificada = mi_decorator(mi_funcion)

# Syntactic sugar
@mi_decorator
def mi_funcion():
    print ('Adios mundo')
