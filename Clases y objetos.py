# Definiendo una clase
class Coche():
    '''Esta clase representa un coche'''
    def __init__(self, modelo, potencia, consumo):
        '''modelo == str
           potencia == int
           consumo == int'''
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._kilometros = 0

    def especificaciones (self):
        '''Muestra las especificaciones del coche'''
        print ('Modelos: ', self._modelo,
               '\nPotencia: ', self._potencia,
               '\nConsumo: ', self._consumo,
               '\nKilómetros: ', self._kilometros)

    def actualizar_km(self,kilometros):
            '''Actualiza los kilómetros'''
            if kilometros > self._kilometros:
                 self._kilometros = kilometros
            else:
             print ('Esos kilómetros no sirven...')

    def actualizar_caballos(self, caballos):
        '''Actualiza los caballos del coche'''
        if caballos > self._potencia:
            self._potencia = caballos
        else:
         print ('El coche no puede ser menos potente...')

    def consumo_total(self):
        '''Calcula el consumo a los 100'''
        consumototal = (self._kilometros / 100) * self._consumo
        print ('El consumo total es: ', consumototal, 'litros...')







mercedes = Coche('mercedes c200', 180, 7)
mercedes.especificaciones()
mercedes.actualizar_km(1000)
mercedes.especificaciones()
mercedes.actualizar_caballos(200)
mercedes.especificaciones()
mercedes.especificaciones()
mercedes.consumo_total()
mercedes.actualizar_km(10000)
mercedes.consumo_total()









