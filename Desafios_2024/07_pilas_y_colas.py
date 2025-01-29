# Pilas y colas

"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Pilas -- LIFO (Last-In, Firs-Out) Stacks
lista1 = []   # Crear lista vacia

print(lista1)

lista1.append(5)   # Añadir elemento (push)
print(lista1)
lista1.append(12)
print(lista1)
lista1.append(59)
print(lista1)

lista1.insert(1, 78)   # Introducir en un puesto determinado un elemento
print(lista1)

print(lista1[0])   # Seleccionar un elemento
print(lista1[1])

lista1.pop()   # Sacar elementos (pop)
print(lista1)
lista1.pop()
print(lista1)
lista1.pop()
print(lista1)


print('########################')
# Colas -- FIFO (First-in, First-Out)  Queue

lista2 = []   # Crear lista vacia

print(lista2)

lista2.append(12)   # introducir elementos al final (enqueue)
print(lista2)
lista2.append(35)
print(lista2)
lista2.append(94)
print(lista2)
lista2.append(105)
print(lista2)

print(lista2[0])   # Seleccionar un elemento
print(lista2[1])

lista2.pop(0)   # Sacar primer elemento (dequeue)
print(lista2)
lista2.pop(0)
print(lista2)
lista2.pop(0)
print(lista2)

print('########################')
from collections import deque   # Importando el módulo queue

lista3 = deque()   # Crear lista vacia

print(lista3)

lista3.append(9)   # introducir elementos al final (enqueue)
print(lista3)
lista3.append(45)
print(lista3)
lista3.append(15)
print(lista3)
lista3.append(125)
print(lista3)

lista3.popleft()   # Sacar primer elemento (dequeue)
print(lista3)
lista3.popleft()   
print(lista3)
lista3.popleft()   
print(lista3)
lista3.popleft()   
print(lista3)


print('########################')
"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.5
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

# navegador web

def web_navigator():
    stack = []

    while True:
        
        action = input("Introduce una url o bien adelante/atrás/salir. ")

        if action == 'salir':
            print("Saliendo del programa.")
            break
        elif action == 'adelante':
            pass
        elif action == 'atrás':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)


        if len(stack)> 0:
            print(f"Actualmente se encuentra en la página {stack[len(stack) - 1]}.")
        else:
            print("Se encuentra en la página de inicio.")


web_navigator()


'''
# mi intento
def web_navigator():
    web_pages = ['web1', 'web2', 'web3', 'web4']
    number = int(input("Introduzca el número de la página web de su historial: "))
    if number < 0 or number > len(web_pages):
        print("El navegador no tiene esa web registrada en el historial.")
    else:
        print(web_pages[number-1])
        option = int(input("Desea navegar 'adelante' [1] o 'atras' [2] de esta página?: "))
        if option == 1:
            adelante = web_pages[number]
            print(adelante)
        elif option == 2:
            atras = web_pages[number-2]
            print(atras)
        else:
            print("Intoduzca una acción válida.")
            return

web_navigator()
'''

# Sistema de impresora

def online_printer():

    queue = []

    while True:
        action = input("Introduzca un documento o imprimir/salir: ")

        if action == 'salir':
            print("Saliendo del programa")
            break
        elif action == 'imprimir':
            if len(queue) > 0:
                print(f"Se está imprimiendo el documento: {queue.pop(0)}")
        else:
            queue.append(action)

        if len(queue) > 0:
            print(f"La cola de documentos a imprimir es: {queue}")
        else:
            print("La cola de impresión se encuentra vacia.")

online_printer()
