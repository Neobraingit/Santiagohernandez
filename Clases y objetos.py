# Definiendo una clase
class Coche():
    '''Esta clase representa un coche'''
    def __init__(self, modelo, potencia, consumo):
        '''Inicializa los atributos de instancia:
             modelo = string
             potencia = entero
             consumo = entero'''
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._kilómetros = 0
    def especificaciones(self):
        '''Muestra las especificaciones del coche'''
        print ('Modelo', self._modelo,
               '\nPotencia',self._potencia,
               '\nconsumo', self._consumo,
               '\nkilómetros',self._kilómetros)

mercedes = Coche('mercedes c200', 180, 7)
mercedes.especificaciones()







