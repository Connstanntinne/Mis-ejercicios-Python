### Listas

# 1. Crea una lista con los números del 1 al 5 e imprí­mela.
list = [1, 2, 3, 4, 5]
print(list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
list = [10, 20, 30, 40, 50]
print(list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprí­mela.
list = [1, 2, 3, 4, 5]
list.append(6)
print(list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
list = [10, 20, 30, 40, 50]
list.insert(2, 15)
print(list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
list = [10, 20, 30, 30, 40, 50]
list.remove(30)
print(list)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5]
#  y almacénalo en una variable. Imprime la variable y la lista.
list = [1, 2, 3, 4, 5]
pop = list.pop()
print(pop)
print(list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprí­mela.
list = [100, 200, 300, 400, 500]
print(list[::-1])

list = [100, 200, 300, 400, 500]
list.reverse()
print(list)


# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprí­mela.
list = [3, 1, 4, 2, 5]
list.sort()
print(list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado 
# en una nueva lista. Imprime la lista resultante.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] 
# que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
list = [10, 20, 30, 40, 50] 
next_list = list[1:3]
print(next_list)

