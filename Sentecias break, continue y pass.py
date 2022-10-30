# ¿Qué es la sentencia break?
'''La podemos utilizar para terminar de forma inmediata la ejecución de una estructura de flujo'''
colores  = ['rojo', 'verde', 'azul']
for color in colores:
    print (color)
    break # En vez de imprimir todos los colores, con break se para a la primera iteración

print ('Esto es una sentencia fuera del bucle for')

'''Lo mismo ocurre con bucles while'''
num = 5
while num <= 5:
    print ('Esto es un buble infinito roto por el break')
    break

# ¿Qué es la sentencia continue?
'''Termina únicamente la ejecución de la iteración actual'''
colores = ['azul', 'verde']
for color in colores:
    print (color)
    continue

# ¿Qué es la sentencia pass?
'''Nos permite definir el esqueleto de distintas estructuras son indicasr ninguna línea de código'''
colores = ['azul', 'verde', 'naranja']
while 'azul' in colores:
    pass
