class Coche ():
    def __init__(self, modelo, marca, caballos):
        self.modelo = modelo
        self.marca = marca
        self.caballos = caballos
        self.kilometros = 0

    def características(self):
        print ('Modelo: ',self.modelo,
        '\nMarca: ', self.marca,
        '\nCaballos: ', self.caballos)


    def modificar_kilometros(self, kilometros):
        if kilometros > 0:
            self.kilometros = kilometros

    def mi_decorador(func):
        def wrapper():
            print ('Antes de la función')
            func()
            print ('Después de la función')
        return wrapper

    @mi_decorador
    def principal():
        print ('Dentro de la función')

    principal()

class electrico(Coche):
    def __init__(self, modelo, marca, caballos):
        super().__init__(modelo, marca,caballos)

toyota = electrico('chr', 'toyota', 122)
toyota.características()



