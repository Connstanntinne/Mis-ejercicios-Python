### Conjuntos

"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
"""
# se utilizan los tipos lista
data = [1, 2, 3, 4, 5]

# añade un elemento
print(data)
data.append(6)
print(data)

# añade un elemento al principio
data.insert(0, 7)
print(data)

# añade varios elementos en bloque al final
data.extend([7, 8])
print(data)

# Añade varios elementos en bloque en una posición concreta
data[2:2] = [23, 34, 45]
print(data)

# Elimina un elemento en una posición concreta
del data[4]
print(data)

#  Actualiza el valor de un elemento en una posición concreta.
data[1] = 99
print(data)

# Comprueba si un elemento está en un conjunto.
print(1 in data)

# limina todo el contenido del conjunto
data.clear()
print(data)


"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {2, 3, 5, 6, 7, 8, 9}

# unión
union_12 = set1.union(set2)
union_13 = set1.union(set3)
union_23 = set2.union(set3)
union_123 = set1.union(set2).union(set3)
print(union_12)
print(union_13)
print(union_23)
print(union_123)

# intersección
print(set1.intersection(set2))
print(set1.intersection(set3))
print(set3.intersection(set2))

# diferencia
print(set1.difference(set2))
print(set2.difference(set1))

# diferencia simétrica
print(set1.symmetric_difference(set2))