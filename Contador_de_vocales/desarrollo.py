def contador ():
    frase = input('Introduce una frase: ')
    frase.lower()
    letra = input('Introduce la letra a contar: ')
    contador = 0
    for i in frase:
     if i in letra:
        contador += 1
        print ('La letra', letra, 'aparece',contador,'veces')
