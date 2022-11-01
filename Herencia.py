class Coche():
    def __init__(self, modelo, caballos, velocidad):
        '''Parámetros:
            modelo == str
            caballos == int
            velocidad == int'''
        self.modelo = modelo
        self.caballos = caballos
        self.velocidad = velocidad


    def modificar_velocidad (self):
        if velocidad > 120:
            print ('Esa velocidad no sirve...')
        else:
            print ('Esa velocidad es la correcta...')


    def estadísticas (self):
        print ('Modelo: ', self.modelo,
               '\nCaballos: ', self.caballos,
               '\nVelocidad: ', self.velocidad)

    def principal():
        print ('Dentro de la función')

    def mi_decorador(func):
        def wrapper():
            print('Antes de la función')
            func()
            print('Después de la función')

        return wrapper

    @mi_decorador
    def principal():
        print('Dentro de la función')

    principal()

Toyota = Coche('chr', 122, 230)
print (Toyota.modelo)
Toyota.estadísticas()

class Electrico (Coche):
    def __init__(self, modelo, caballos, velocidad):
        super().__init__(modelo, caballos, velocidad)


seat = Electrico('marbella', 180,134)
seat.estadísticas()
print (seat.modelo)





