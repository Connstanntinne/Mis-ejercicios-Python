### Expresiones regulares

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
"""

import re

text = "La casa de la cigarra estaba a 30 pasos de la hormiga. Vivían 4 cigarras. También vivían 456 hormigas."
print(text)

# match
match = re.match('La casa de la cigarra', text, re.I)
print(match)
start, end = match.span()
print(text[start:end])

match2 = re.match('pasos de la hormiga', text, re.I)
print(match2)


# search
search = re.search('casa de la cigarra', text, re.I)
print(search)
start, end = search.span()
print(text[start:end])

# findall

findall = re.findall('hormiga.', text)
print(findall)

# split
split = re.split('\.', text)
print(split)

# sub
sub = re.sub('cigarra', 'araña', text)
print(sub)



# expresiones regulares
pattern = r"[0-9]+"   # r"\d+"
findall = re.findall(pattern, text)
print(findall)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
email = r"^[a-zA-A0-9._-]+@[a-zA-Z0-9]\.[a-z0-9.]+$"
phone_number = r"^[+\d]?[\d\s]{3,}$"
url = r"^http[s]?://(www.)?[a-zA-Z0-9./_-]+\.[a-zA-Z]+$"

prueba = "https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md"

findall = re.findall(url, prueba, re.I)
print(findall)



