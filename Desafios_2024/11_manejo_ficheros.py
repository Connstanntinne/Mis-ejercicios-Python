### Manejo de ficheros .txt

"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
"""

import os

with open("Desafios_2024/my_file.txt", 'w') as file:
    file.write('Mi nombre es Óscar\nMi edad es 46 años\nMi lenguaje de programación favorito es Python')

with open("Desafios_2024/my_file.txt", 'r') as file:
    print(file.read())

os.remove('Desafios_2024\my_file.txt')

print('######################')

"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""


def sales_management():
    file = open('Desafios_2024\sales_management.txt', 'w', encoding='utf-8')
    file.close()
    print("Bienvenido a tu gestor de ventas.")
    

    while True:
        print("Elige una opción.")
        print("1. Añadir producto: ")
        print("2. Consultar producto: ")
        print("3. Actualizar producto: ")
        print("4. Eliminar producto: ")
        print("5. Mostrar productos: ")
        print("6. Calcular venta total: ")
        print("7. Calcular venta por producto: ")
        print("8. Salir. ")

        option = input("Seleccione una opción: ")

        if option == '1':   # Añadir producto
            product_name = input("Nombre del producto: ")
            amount_saled = input("Cantidad vendida: ")
            price = input("Precio: ")
            with open('Desafios_2024\sales_management.txt', 'a') as file:
                file.write(f"{product_name}, {amount_saled}, {price}\n")

        elif option == '2':   # Consultar producto
            product_name = input("Nombre del producto: ")
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                for line in file.readlines():
                    if line.split(', ')[0] == product_name:
                        print(line)
                        break
                    else:
                        print("Producto no encontrado.")

        elif option == '3':   # Actualizar producto
            product_name = input("Nombre del producto: ")
            amount_saled = input("Cantidad vendida: ")
            price = input("Precio: ")
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                lines = file.readlines()
            with open('Desafios_2024\sales_management.txt', 'w') as file:
                for line in lines:
                    if line.split(', ')[0] == product_name:
                        file.write(f"{product_name}, {amount_saled}, {price}\n")
                    else:
                        file.write(line)

        elif option == '4':   # Eliminar producto
            product_name = input("Nombre del producto: ")
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                lines = file.readlines()
            with open('Desafios_2024\sales_management.txt', 'w') as file:
                for line in lines:
                    if line.split(', ')[0] != product_name:
                        file.write(line)

        elif option == '5':   # Mostrar productos
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                print(file.read())

        elif option == '6':   # Calcular venta total
            total = 0
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                for line in file.readlines():
                    #total += int(line.split(', ')[1]) * int(line.split(', ')[2])
                    components = line.split(', ')
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(f"La venta total es: {total} €.")

        elif option == '7':   # Calcular venta por producto
            product_name = input("Nombre del producto: ")
            total = 0
            with open('Desafios_2024\sales_management.txt', 'r') as file:
                for line in file.readlines():
                    components = line.split(', ')
                    if components[0] == product_name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
            print(f"La venta del producto {product_name} es: {total} €.")

        elif option == '8':   # Salir
            print("Saliendo del programa.")
            os.remove('Desafios_2024\sales_management.txt')
            break

        else:   # Opción no válida
            print("Seleccione una opción 1-8.\n")


sales_management()