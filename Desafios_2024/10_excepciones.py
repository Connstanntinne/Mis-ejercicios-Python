# Excepciones

"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

def division(number1: int, number2: int):
    try:
        print(number1 / number2)
    except Exception as error:
        print(f"Error: {error}")

division(2, 4)
division(2, 0)

print("#####################")

def list_access(list, index):
    try:
        print(list[index])
    except Exception as error:
        print(f"Error: {error}")

list_access([1, 2, 3, 4], 3)
list_access([1, 2, 3, 4], 6)
print("#####################")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""
class NegativeNumError(Exception):
    pass


def division(num1, num2):
    try:
        if num1 <0 or num2 < 0:
            raise NegativeNumError("No vamos a dividir números negativos.")
        print(num1 / num2)
    except TypeError as e:
        print(e)
        print("Uno de los valores introducidos es un str.")
    except ZeroDivisionError as e:
        print(e)
        print("No se puede dividir entre '0'.")
    except NegativeNumError as e:
        print(e)
        print("Uno de los valores introducidos es negativo.")
    else:
        print("Enhorabuena!!! No se ha producido ningún error.")
    finally:
        print("La ejecucción ha finalizado\n")


division(1 , 5)
division(1 , 'casa')
division(1 , -5)
division(-1 , 5)
division(1 , 0)