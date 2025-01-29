### Callbacks
"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""
# 1. pasamos una función como argumento de otra función
# 2. llamamos a una función dentro de otra función

# En 'built-in' functions:

list = ["lmn", "AbCd", "khJH", "eort", "SuNnY"]
print(sorted(list))     
print(sorted(list, key=str.lower))    # ejecutamos la función lower() y tras ella sorted()


# En 'user-definded' functions:

def called(num : int):
    print("Esta es la función called.")
    return num ** 3

def caller(function, num: int):
    print("Esta es la función caller.")
    return function(num)

print(caller(called, 5))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
"""
import time
import random
import threading


def order_process(order, confirmation_callback, ready_callback, delivered_callback):
    def process():
        confirmation_callback(order)
        time.sleep(random.randint(1,10))
        ready_callback(order)
        time.sleep(random.randint(1,10))
        delivered_callback(order)
    threading.Thread(target=process).start()     # Módulo para ejecutar funciones en paralelo


def confirmation(order):
    print(f"El pedido de {order} se encuentra confirmado.")
        

def ready(order):
    print(f"El pedido de {order} se encuentra listo.")

def delivered(order):
    print(f"El pedido de {order} se encuentra entregado.")


order_process("Cocido", confirmation, ready, delivered)
order_process("Pizza Napolitana", confirmation, ready, delivered)
order_process("Pizza 4 quesos", confirmation, ready, delivered)
order_process("Kebab", confirmation, ready, delivered)
order_process("Sandwich mixto", confirmation, ready, delivered)





