# Clases

"""
* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Clase:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def imprimir(self):
        print(self.atributo1)
        print(self.atributo2)

clase = Clase('perro', 'gato')
clase.imprimir()


clase.atributo1 = 'atributo 1'
clase.atributo2 = 'atributo 2'

clase.imprimir()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, new_item):
        self.stack.append(new_item)

    def pop(self):
        if self.count() > 0:
            self.stack.pop()
        else:
            return None
            print("La pila no tiene elementos que eliminar.")

    def count(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

        for item in reversed(self.stack):
            print(item)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, new_iteM):
        self.queue.append(new_iteM)

    def dequeue(self):
        if self.count() > 0:
            self.queue.pop(0)
        else:
            return None
            print("La cola se encuentra vacía.")

    def count(self):
        return len(self.queue)
    
    def print_queue(self):
        print(self.queue)

        for item in self.queue:
            print(item)

print('------------')

pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)

pila.print_stack()

pila.pop()
pila.print_stack()
print(pila.count())

print('------------')

cola = Queue()
cola.enqueue('coche')
cola.enqueue('perro')
cola.enqueue('tomate')

cola.print_queue()

cola.dequeue()
cola.print_queue()
print(cola.count())

