
# Valor y Referencia

"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""

'''
Los datos que le pasamos a una función pueden ser:
- por valor: el elemento es único.
             se crea una copia local de la variabre dentro de la función.
             no se modifica la variable externa.
             se pasan valores simples (primitivos) tipo: entero, flotante, cadena, lógicos...
- por referencia: se maneja directamente la variable.
                  los cambios realizados dentro de la función también afectarán fuera.
                  se pasan valores complejos tipo: lista, tupla, set, diccionario...
                  heredan su posición den la memoria.
'''

# por valor

valor = 10
def double(numero : int):
    return numero * 2

print(double(valor))
print(valor)


my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)


# por referencia
numeros = [1, 2, 3, 4]
def añadir_valor(numero : int):
    numeros.append(7)
    print(numeros)

añadir_valor(numeros)
print(numeros)


ns = [10,50,100]
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2 
    print(numeros)

doblar_valores(ns)
print(ns)


my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)


# para modificar los tipos simples, modificarlos y reasignarlos

n = 25
def double(numero : int):
    return n * 2

print(double(n))

n = double(n)
print(n)

# para los tipos compuestos, podemos evitar la modificación enviando una copia:

ns = [10,50,100]
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
    print(numeros)

doblar_valores(ns[:])   # Una copia al vuelo de una lista [:]
doblar_valores(ns.copy())  # Una copia al vuelo de una lista list.copy()
ns_copy = list(ns)
doblar_valores(ns_copy)   # Una copia al vuelo de una lista usando el constructor
print(ns)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

# por valor:

x = 13
y = 28
def variable_interchange(n1 : int, n2: int):
    x = n2
    y = n1
    print(f"La variable x tiene el valor {x} dentro de la función.")
    print(f"La variable y tiene el valor {y} dentro de la función.")

variable_interchange(x, y)
print(x)
print(y)
print(f"Fuera de la función las variables mantienen su valores x,y: {x}, {y}.\n")



def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")


# por referencia:
list1 = [1, 3, 5, 7]
list2 = ['casa', 'coche', 'perro']
def list_interchange(l1 : list, l2: list):
    list1 = l2
    list2 = l1
    print(f"La list1 tiene el valor {list1} dentro de la función.")
    print(f"La list2 y tiene el valor {list2} dentro de la función.")

list_interchange(list1, list2)
print(list1)
print(list2)
print(f"Fuera de la función las listas tiene sus valores list1 y list2: {list1}, {list2}.\n")


def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")
