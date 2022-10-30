# ¿Qué es el scope y el namespace en Python?
'''Un namespace es un mapeo de nombres a objetos.'''
# Namespace por defecto
print (dir(__builtins__))

# Namespace global
modulo = 10
print (globals())

# Namespace local
def func():
    var = 5
    print (locals())

func()

# ¿Qué es el scope en Python?
'''Es una región del programa donde un namespace es accesible'''
# Scope local
def func():
    var_local_func = 10
    print (var_local_func)
pace
func()

# Scope no local
''' Es un ámbito especial que solo existe para las funciones anidadas'''
def func2 ():
    no_local_func2 = 10
    print ('Namespaces func2', locals())
    def func3 ():
        print ('Namespaces funk3', locals())
        var_local_func3 = 5

func2()