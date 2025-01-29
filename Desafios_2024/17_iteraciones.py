### Iteraciones

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""
# 1 for
for n in range(1,11):
    print(n)

#2 for con lista
list_num = (list(range(1,11)))
for i in list_num:
    print(i)

# 3 while
number = 1
while number < 11:
    print(number)
    number +=1

# 4  función recursiva
def count(i=1):
    if i < 11:
        print(i)
        count(i + 1)

count()

"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")