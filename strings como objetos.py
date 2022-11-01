texto = 'cadena de texto'
print (texto.upper()) # Convertimos en mayúsculas
print (texto.lower()) # Convierte en minúsculas
print (texto.capitalize()) # Pone en mayúsculas la primera letra
print (texto.title()) # Hace un título poniendo todas las palabras con la primera letra en mayúsculas
print (texto.swapcase())# Intercambia las letras entre mayúsculas y minúsculas

# Buscar y reemplazar subcadenas
print (texto.count('o')) # Busca cuantas veces se repite la letra o
print (texto.find('o')) # No muestra el índice donde está la subcadena o la letra que le pasemos
print (texto.rfind('o')) # Busca la letra empezando por el final

# Clasificación de caracteres
print (texto.isalnum()) # Nos muestra si son todos los caracteres alfanuméricos
print (texto.isdigit()) # Nos muestra si todos los caracteres son números

# String formatting
print (texto.center(20)) # Me centra el texto en el número de caracteres con el número que yo le pase
print (texto.ljust(20)) # Justifica el texto a la izquierda
print (texto.lstrip()) # Elimina los especios por la izquierda
print (texto.rstrip()) # Elimina los espacios por la derecha
print (texto.strip())  # Quita los espacios de los lados
print (texto.replace(' ', '_')) # Reemplaza los espacios por lo que le digamos
print (texto.zfill(10)) # Mete ceros a la ixzquierda de la cadena de números

# Concatenar un string con un objeto iterable
print (','.join(['Marcos', 'Carmona'])) # Introduce un caracter que le pasemos a la cadena concatenando

