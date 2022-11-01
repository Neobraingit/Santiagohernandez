# Números como objetos y sus métodos
num = 12
# A partir de un nùmero lo convertimos en hexadecimal
print (num.to_bytes(3, 'big')) # numero que quiero sacar, orden
print (num.from_bytes(b'\x00\x00\x0c,  'big')) # hace lo contrario que el anterior