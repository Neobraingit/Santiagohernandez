# Implementar la agenda y los contactos
agenda_digital = {
    # Primer contacto de la agenda
    'Marcos Carmona' : {
        'direccion': 'Santirso de abres',
        'email' : 'Maervca2@icloud.com',
        'Teléfono' : '615072086'
    },
    # Segundo contacto de la agenda
    'Eva Alonso' : {
        'direccion' : 'San tirso de abres',
        'email' : 'evalonrez@icloud.com',
        'Teléfono' : '123456789'
    }
}

# Escribir la agenda en disco con una función
def escribir_agenda (nombre_Agenda, agenda_digital):
    '''nombre_agenda se corresponde con el nombre del fichero en el disco
       agenda_digital se corresponde con la agenda digital y los contactos'''
    agenda_fichero = open('nombre_agenda', 'w')
    agenda_fichero.write(str(agenda_digital))
    agenda_fichero.close()

escribir_agenda('Agenda', agenda_digital)

# Leer el fichero creado y guardado
agenda_digital_lectura =open('nombre_agenda', 'r')
agenda_digital = agenda_digital_lectura.readlines()
agenda_digital_lectura.close()
print (agenda_digital)

# Crear un menú para introducir un nombre en la agenda
def solicitar_contacto():
    '''Esta función solicita los datos de un nuevo contacto'''
    nombre = input('Introduce el nombre: ')
    dirección = input('Introduce la dirección del nuevo contacto: ')
    email = input('Introduzca el email: ')
    teléfono = input('Introduce el teléfono del contacto')
    # Construimos un diccionario con los valores recibidos
    nuevo_contacto = {
        'nombre' : nombre,
        'dirección' : dirección,
        'email' : email,
        'teléfono' : teléfono
    }
    return nuevo_contacto

nuevo_contacto = solicitar_contacto()
print (agenda_digital)








