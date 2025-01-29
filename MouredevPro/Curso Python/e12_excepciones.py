# Manejo de Excepciones

# 1. Crea una función que intente dividir dos números proporcionados por el usuario. 
# Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
print('######################')

def division(num1: int, num2: int):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")

division(2, 5)
division(5, 2)
division(2, 0)

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. 
# Usa try-except para capturar cualquier error en la conversión.
print('######################')

def str_conversor(string : str):
    try:
        string = int(string)
        print(string)
    except Exception as error:
        print(error)

str_conversor('17')
str_conversor('256')
str_conversor('paloma')


# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores 
# (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones 
# de archivos de forma segura.
print('######################')

def file_manager(file_name : str):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: el archivo no pudo ser encontrado.")


file_manager('excepciones.txt')
file_manager('excepciones2.txt')


# 4. Crea una función que realice múltiples operaciones 
# (suma, resta, división, multiplicación) con dos números. 
# Usa try-except-else-finally para manejar errores y asegurar que 
# se imprima un mensaje final, independientemente de los errores.
print('######################')

def calculator(num1: int, num2: int):
    try:
        print(num1 + num2)
        print(num1 - num2)
        print(num1 * num2)
        print(num1 / num2)
    except Exception as error:
        print('No se ha podido realizar una de las operaciones')
        print(error)
    else:
        print("Todas las operaciones han sido realizadas con éxito.")
    finally:
        print("Todos los procesos han terminado.")

calculator(2, 9)
calculator(12, 7)
calculator(2, 0)


# 5. Crea una función que le pida al usuario su edad y lance un ValueError si
# la entrada no es un número entero positivo. Usa el manejo de excepciones para
# gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
print('######################')

def ask_age():
    try:
        age = int(input("Introduzca su edad: "))
        if age <= 0:
            raise ValueError("La edad debe ser un entero positivo.")
        return age

    except ValueError as error:
        print(f"Error: {error}")

ask_age()


# 6. Crea una función que intente acceder a un elemento de una lista por ídice. 
# Usa try-except para manejar el caso donde el ídice está fuera de rango.
print('######################')

def list_access(list, index):
    try:
        return list[index]
    except IndexError:
        print("Error: Índice fuera de rango. ")

list_access(['1', '2', '3', 'mesa', '5'], 2)
list_access(['1', '2', '3', 'mesa', '5'], 8)


# 7. Crea una función que use try-except para manejar múltiples 
# excepciones: ZeroDivisionError, ValueError y TypeError.
print('######################')

def my_function():
    try:
        print("Todo funciona correctamente")
    except ZeroDivisionError as error:
        print(error)
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)

my_function()


# 8. Crea una función que simule una transacción. Lanza una excepción personalizada 
# llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
print('######################')

class InsufficientFundsError(Exception):
    pass

def transaction(saving, retire_funds):
    try:
        if retire_funds <= saving:
            saving -= retire_funds
            print(f"Ha retirado {retire_funds} €. Actualmente quedan {saving} € en su cuenta.")
        else: 
            raise InsufficientFundsError("Saldo insuficiente.")

    except InsufficientFundsError as error:
        print(f"Error: {error}")

    finally:
        print("Hasta la próxima.")

transaction(5000, 200)
transaction(5000, 7000)


# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error 
# que surja cuando una cadena no pueda convertirse.
print('######################')

def list_int_conversor(string_list):
    #list = ['1', '2', '3', 'mesa', '5']
    #list = ['1', '2', '3', '4', '5']
    integers = []
    for string in string_list:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se poslible transformarlo en entero.")
    return integers

list_int_conversor(['1', '2', '3', 'mesa', '5'])
list_int_conversor(['1', '2', '3', '4', '5'])


# 10. Crea una función que calcule la raí­z cuadrada de un número. 
# Lanza un ValueError si el número es negativo.
print('######################')

def sqrt_numb(numb):
    try:
        if numb < 0:
            raise ValueError (
                "No puede calcularse la raíz cuadrada de un negativo.")
        return numb ** 0.5
    except ValueError as error:
            print(f"Error: {error}")

sqrt_numb(9)
sqrt_numb(-5)
