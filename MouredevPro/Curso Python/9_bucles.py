### Bucles

# 1. Usa un bucle while para imprimir los números del 1 al 10.

number = 1
while number < 11:
    print(number)
    number += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.

lista = [10, 20, 30, 40, 50]
for i in lista:
    print(i)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

number = 1
suma = 0
while number < 101:
    print(suma)
    suma += number
    number +=1

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".

name = "Python"
for n in name:
    print(n)


# 5. Usa un bucle while para encontrar el primer numero divisible por 7 entre 1 y 50.

number = 1
while number < 51:
    print(number)
    number += 1
    if number % 7 == 0:
        print(f"El número {number} es el primer divisible entre 7. ")
        break

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} 
# e imprime las claves.

dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for i in dict:
    print(i)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

number = 1
while number < 21:
    if number % 2 == 0:
        print(number)
    number += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.

for n in range(10,0,-1):
    print(n)


# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece
#  el número 30 en la lista[30, 10, 30, 20, 30, 40].

list = [30, 10, 30, 20, 30, 40]
treintas = []
for n in list:
    if n == 30:
        treintas.append(n)
print(treintas)
print(len(treintas))
print(f"El número 30 aparece {len(treintas)} veces en lista.")


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

nombres = ['Carlos', 'Juan', 'Manuel', 'Brais', 'roberto', 'Anibal']
for name in nombres:
    print(name)
    if name == 'Brais':
        print("El nombre 'Brais' fué encontrado")
        break

