### Pruebas unitarias

"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.

"""

def sum_two(num1: int, num2: int):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        print("Esta función solamente sumará números enteros.")

print(sum_two(3, 5))
print(sum_two(3.2, 5))
print(sum_two('mesa', 5))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

my_dict = {
    'name': 'Oscar',
    'age': 46,
    'birth_date': '17 de agosto de 1978',
    'programing_languages': ['Python', 'C++']
}

print(my_dict)