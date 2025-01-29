
# Cadenas de Caracteres.

"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
"""

# como crear una string 
my_string = "Esta es una cadena con comillas dobles"   # comillas dobles
my_othrer_string = 'Esta es una cadena con comillas simples'   # comillas simples
another_string = "1254"   # los números pueden ser del tipo str

print(my_string)
print(my_othrer_string)
print(another_string)

print(type(my_string))
print(type(my_othrer_string))
print(type(another_string))

# como salvar "" y ''
my_string = "Ella le dijo \"Si\"."   # empleando \" o \' dependiendo de la construcción"
print(my_string)
my_string = 'Ella le dijo "Si".'   # alternando ambos constructores
print(my_string)

# métodos de escape
my_string = "El coche era de su padre.\nNo se lo iba a dejar."   # para saltar línea
print(my_string)
my_string = "\tTabulamos una vez el texto."   # tabular texto
print(my_string)
my_string = "\t\tTabulamos dos veces el texto."
print(my_string)

# str en múltiples líneas, con """ o '''
multiples_lines = """
Este es un texto en múltiples líneas  
y se escribirá de forma ordenada
tal y como lo definamos.
"""
print(multiples_lines)

# Operaciones con str
print("casa" * 3)
print("casa" "grande")
print("casa" + "grande")
print("co" *2 + "ro" + "co")

my_string = "casa"
print(my_string)
my_string = "casa" * 3
print(my_string)
my_string = my_string * 2
print(my_string)
my_othrer_string = ("Esta es una str muy larga y me voy a tener que " 
                    "ver obligado a partirla en dos.")
print(my_othrer_string)


# las str pueden ser indexadas
my_string = 'cachorro'
print(my_string[0])   # accedemos a uno de los elementos
print(my_string[3])
print(my_string[-2])

# función slicer:
print(my_string[0:4])   # accedemos a varios elementos 
print(my_string[1:])
print(my_string[1:-2])
print(my_string[:6])

# recordar s[:i] + s[i:] = s[:]
my_string = 'cachorro'
string = (my_string[:4])
other_string = (my_string[4:])
sum_string = (string + other_string)
print(string)
print(other_string)
print(sum_string)

# reverso de str
print(my_string[::-1])

# str es inmutable
my_string = 'cachorro'
# my_string[2] = 'l'    # no podemos modificar un str

# acepta la función len()
print(len(my_string))

# str methods
print(my_string.capitalize())   # primera letra en mayúsculas
print(my_string.upper())   # todas las letras en mayúsculas (opuesto .lower())
print(my_string.count('o'))   # cuenta cuantas  veces se encuentra un elemento en el str
print(my_string.endswith('rro'))   # verdadero si termina de determinada forma el str
print(my_string.find('cho'))   # busca unos elementos y nos dice en que posición se encuentran en el str
print('cho' in my_string)   # para saber si un elemento se encuentra en el str
print('mi coche es de color {}.'.format('verde'))   # da formato al str y permite sustituir {}
print(my_string.index('ach'))   # similar a find
print(my_string.isalnum())   # si todo el str es alfanumérico
print(my_string.isalpha())   # si todo el str se encuentra en el alfabeto
print(my_string.isdigit())   # si todo el str es numérico
print(my_string.islower())   # si todo el str es en minúsculas 
print(my_string.isupper())   # si todo el str es en mayúsculas
print(my_string.istitle())   # si primera letra en mayúsculas y resto en minúscular
print('#'.join(my_string))   # añade iterable
print(my_string.partition('ho'))   # crea tupla segmentando la str según orden
print(my_string.removeprefix('ca'))   # eliminar prefijo
print(my_string.removesuffix('rro'))   # eliminar sufijo
print(my_string.replace('cho', 'mo'))   # crea nuevo str reemplazando
print(my_othrer_string.split(' '))   # crea tupla separando el str según orden indicada
print(my_string.startswith('ca'))   # si empieza por
print('  La casa es azul  '.strip())   # elimina espacios


# print sting formatting
print("El %s es del año %d." % ('coche', 2005))

# f-str
print(f'Pluto es nuestro {my_string}.')

# crear lista
print(list(my_string))   # separar str en list
print(''.join(list(my_string)))   # unir lista para hacer str

# crear set
print(set(my_string))


### EJERCICIO EXTRA
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

def words_comparer(word1 : str, word2 : str):

    # palíndromo
    print(f"La palabra {word1} es un palindromo: {word1 == word1[::-1]}")
    print(f"La palabra {word2} es un palindromo: {word2 == word2[::-1]}")
    
    # anagrama
    print(f"La palabra {word1} y la palabra {word2} son anagrama: {sorted(word1) == sorted(word2)}")

    # isograma
    def isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) +1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")




words_comparer("radar", "casa")
words_comparer("casa", "saca")
words_comparer("casacasacasa", "saca")