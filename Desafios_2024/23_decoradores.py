### Patrones de diseño: decoradores
"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

def decorador(function):
    def wrapper(*args, **kwargs):
        print("Aplicando el decorador antes de la función")
        result = function(*args, **kwargs)
        print("aplicando el decorador tras la función")

        return result
    
    return wrapper

@decorador
def sum(a, b):
    print("Ejecutándose la función.")
    
    return a + b

print(sum(2, 9))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""
print('====================================')


def count_function(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        wrapper.count += 1
        print(f"La función {function.__name__} ha sido llamada {wrapper.count} veces.")

        return result
    wrapper.count = 0
    return wrapper


@count_function
def sum(a, b):
    
    return a + b

print(sum(51, 52))
sum(2, 9)
sum(8, 9)
print(sum(2, 5))
