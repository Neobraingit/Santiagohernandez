set = {'valor1', 'valor2', 'valor3'}
set2= { 'valor4', 'valor5', 'valor6'}

# Operaciones con sets
# Intersección entre dos conjuntos
print (set.intersection(set2))

# Union de sets
print (set.union(set2)) # Junta dos sets peros sin orden

# Subconjunto de un conjunto
print (set.issubset(set2))

# Diferencia entre ambos conjuntos
print (set.symmetric_difference((set2)))
