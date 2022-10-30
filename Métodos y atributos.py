# ¿Qué son los métodos?
'''Cuando una función forma parte de una clase se le denomina método'''
class Coche:
    atributoclase = 150 # Esto es una atributo de clase
    def __init__(self):

     def velocidad_máxima(self):
        '''Este método devuelve la velocidad del coche'''
        print ('Velocidad máxima: ??')

Renault = Coche()
BMW = Coche()


class Casa:
    def __init__(self, colores):
        self.colores = colores
    def colores(self):
            '''Esto de vuelve los colores'''
            print ('El color es: ', self.colores)




apartamento = Casa('rojo')
print (apartamento.colores)
adosado = Casa('amarillo')
print (adosado.colores)






