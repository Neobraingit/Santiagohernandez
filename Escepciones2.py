# Exception Assertionerror
paswd = input('Contraseña de más de 8 dígitos: ')
assert len(paswd) > 8, 'la contraseña no tiene los suficientes dígitos...'

# Cláusula else en excepciones:
try:
    var = 2
except NameError:
    print ('La variable no está definida...')
    var = 'hola mundo'
else:
    print ('La variable ya está definida')

# Sentencia finally
try:
    var = 2
except NameError:
    print ('La variable no está definida...')
    var2 = 'hola mundo'
else:
    print ('La variable ya está definida')
finally:
    del var2
