# String son cadenas de texto
var = 'Esto es un string'
var2 = '123445'  # Esto es un string por que va entre comillas

# Indexación es acceder a un elemento en particular mediante un índice o valor
print (var[1]) # Accedemos  al índice uno que corresponde a la s
print (var[-1]) # Contamos desde atrás

# Slicing es extraer subcadenas de una cadena de texto
print (var[0:4]) # Extraemos desde el cero hasta el cuatro sin ser incluido el último valor
# Si no indicamos uno de los índices irá hasta el final
print (var[0:])

# Stride es una variante del Slicing. Si se añade otros : lo hará en los saltos indicados
print (var[0:4:2]) # Irá desde el cero hasta el tres en saltos de dos

# Modificación de strings
# No podemos modificar una parte de un string, pero si podemos cambiar el valor de una variable
var3 = 'Marcos'
var3 = 'Eva'
print (var3)

# Strings de múltiples líneas. Lo hacemos con \n
var4 = 'Marcos\nCarmona\nGarcía'
print (var4)

