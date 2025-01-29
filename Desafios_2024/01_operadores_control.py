# Operadores y estructuras de control

# Crear ejemplos utilizando todos los tipos de operadores del lenguaje

my_str = 'esta es una cadena'
my_other_str = 'esta es otra cadena'
'''operadores con cadenas'''
print (my_str + ' y ' + my_other_str)
print (my_other_str * 4)

my_number = 5
my_other_number = 13

''' operadores aritméticos'''
print (my_number + my_other_number)
print (my_number - my_other_number)
print (my_number * my_other_number)
print (my_number / my_other_number)
print (my_number + my_other_number)
print (my_number ** 3)

'''operadores lógicos y de comparación'''
print (my_number < my_other_number)
print (my_number <= my_other_number)
print (my_number > my_other_number)
print (my_number >= my_other_number)
print (my_number == my_other_number)
print (my_number != my_other_number)


### Crea un programa que imprima por consola todos los números comprendidos
### entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print('FOR')
print("ejercicio con operadores")
for n in range(10,56):
    if n == 16:
        continue
    elif n % 3 == 0:
        continue
    elif n % 2 == 0:
        print(n, end = ' ')

print("\ncompacto")
for n in range(10, 56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n, end = ' ')

print('\nWHILE')
number = 10 
while number <= 55:
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number, end = ' ')
    number += 1
