### Funciones y alcance

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""


def print_number(first_word, second_word):
    printed_number= 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(first_word + second_word)
        elif number % 3 == 0:
            print(first_word)
        elif number % 5 == 0:
            print(second_word)
        else:
            print(number)
            printed_number += 1
            
    return print("El número de veces que se ha imprimido un número es:", printed_number)



print_number('tres', 'cinco')
