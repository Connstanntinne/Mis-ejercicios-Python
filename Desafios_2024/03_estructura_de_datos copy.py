### Estructura de datos

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


def agenda_contactos():

    contacts = dict()

    def add_contact():
        name = input("Nombre: ")
        phone = input ("Número de teléfono: ")
        if phone.isdigit() and len(phone) >0 and len(phone) <= 11:
            contacts[name] = phone
        else:
            print("Introduzca un número menor o igual a 11 dígitos.")

    while True:
        print("\nEsta es una agenda de contactos.")
        print("1. Busqueda: ")
        print("2. Nuevo contacto: ")
        print("3. Actualización de contacto: ")
        print("4. Eliminación de contacto: ")
        print("5. Salir. ")

        action = input("\nSeleccione una de las opciones: ")

        match action:
            case "1":
                name = input("nombre: ")
                if name in contacts:
                    print(f"El número de teléfono de {name} es: {contacts[name]}")

                else:
                    print(f"El contacto {name} no se ha encontrado.")

            case "2":
                add_contact()

            case "3":
                add_contact()

            case "4":
                name = input("Nombre: ")
                if name in contacts:
                    del contacts[name]
                    print("El contacto se eliminó.")
                else:
                    print(f"El contacto {name} no se ha encontrado.")

            case "5":
                print("Gracias por usar la agenda. Hasta pronto.")
                break
            
            case _:
                print("Elija una opción válida.")



agenda_contactos()