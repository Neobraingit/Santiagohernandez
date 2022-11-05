from paquetenuevo.modulo1 import *
from paquetenuevo.modulo2 import  *

coche1 = Coche('chr', 'Toyota', 'Blanco')
coche1.características()
coche1.modificar_kilometros(100)
print(coche1.kilometros)

coche2 = Electrico('MODEL3', 'TESLA', 'ROJO')
coche2.características()
print (coche2.color)
coche2.características()
coche2.modificar_kilometros(300)
print (coche2.kilometros)
coche2.características()


