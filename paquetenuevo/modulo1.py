class Coche():
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        kilometros = 0

    def modificar_kilometros(self, kilometrosnuevos):
        if kilometrosnuevos > 0:
            self.kilometros = kilometrosnuevos

    def características(self):
        print ('Modelo: ', self.modelo,
               '\nMarca: ', self.marca,
               '\nColor: ', self.color)
    def midecorador(func):
        def wrapper():
            print ('Antes de la función...')
            func()
            print ('Después de la función...')
        return wrapper
    @midecorador
    def prueba():
        print ('Dentro de la función...')
    prueba()

class Electrico (Coche):
    def __init__(self, modelo, marca, color):
        super().__init__(modelo,marca,color)

