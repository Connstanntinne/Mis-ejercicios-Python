
# Recursividad


"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def cuenta_atras(num : int):
    if num < 0:
        print("Se acabó la cuenta atrás.")
        return 0
    else:
        print(num)
        cuenta_atras(num -1)

cuenta_atras(100)


def cuenta_atras(num : int):
    if num >= 0:
        print(num)
        cuenta_atras(num -1)

cuenta_atras(25)



def cuenta_regresiva(numero : int):   # vemos el flujo de los datos
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero - 1)
    else:
        print("¡Boooooooom!")
    print("Fin de la función", numero)

cuenta_regresiva(5)


# otros ejemplos para entender la recursividad
def serie_numeros(num : int):   
    if num > 0:
        serie_numeros(num - 1)   # al cambiar el orden de la llamada a función y print
        print(num)               # vemos como invierte el orden de aparición de los datos
        

serie_numeros(7)



def factorial(numero):
    print("Valor inicial ->", numero)   # ejemplo para ver el flujo de la función
    if numero > 1:
        numero = numero * factorial(numero - 1)
    print("valor final ->", numero)
    return numero

print(factorial(6))





"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

# factorial:

def factorial(num : int) -> int:
    if num < 0:
        print("los números negativos no son válidos.")
        return 0
    elif num == 0:
        return 1
    else:
        valor = num * factorial(num - 1)
        return valor
    

print(factorial(5))
print(f"El factorial de 5 es {factorial(5)}")


# factorial sin recursividad:
def factorial(n):
    if n==0: return print(1)
    for x in range (1,n):
        n=n*x
    return print(n)

factorial(5)



# fibonachi:
def fibonachi(num : int)-> int:
    if num <= 0:
        print("La posición tiente que ser mayor que cero.")
        return 0
    elif num == 1:
        return 0
    elif num == 2: 
        return 1
    else:
        valor = fibonachi(num - 1) + fibonachi(num -2)
        return valor

print(fibonachi(7))
print(f"El puesto número 7 en la serie de fibonachi es: {fibonachi(7)}")




# fibonachi sin recursividad

def fibonachi(numero):
    resultado = []
    a , b = 0, 1
    for i in range(numero):
        resultado.append(a)
        a , b = b , a + b
    print(resultado)

fibonachi(10)




