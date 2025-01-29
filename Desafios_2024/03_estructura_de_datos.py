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




'''
names = [1, 2, 3]
phone_numbs = [6, 7, 8]
contacts = dict(zip(names, phone_numbs))

print(contacts)
'''
contacts = dict()




def add_contact():
    '''Función para introducir contactos'''
    new_name = input("Nombre: ")
    if new_name.lower in contacts:
        print("\nYa guardaste ese contacto.")

    new_phone = input("\nIntroduzca el número de teléfono: ")
    if len(new_phone) <= 11 and new_phone.isdigit:
        contacts[new_name.lower] = new_phone
        print("\nEl contacto ha sido guardado correctamente.")
    
    else:
        print("\nDebe introducir un número válido menor o igual a 11 dígitos.")




def search():
    '''Función para búsqueda de contactos y su guardado si es nuevo'''
    search_name = input("Introduce el contacto que estás buscando: ")

    if search_name in contacts:
        print("\nYa guardaste ese contacto.")
        print(f("\nEn número de teléfono de {search_name} es {contacts[search_name]}"))



def show_menu():
    print("\nEsta es una agenda de contactos. Guardaremos nombre y número de teléfono.")
    print("1. Busqueda: ")
    print("2. Nuevo contacto: ")
    print("3. Actualización de contacto: ")
    print("4. Eliminación de contacto: ")
    print("5. Salir. ")





while True:
    
    show_menu()

    action = input("Seleccione un número: ")
    if action == "1":
        if len(contacts) == 0:
            print("\nNo disponemos de ningún contacto guardado.")
        else:
            search()


    elif action == "2":
        add_contact()


    elif action == "3":
        if len(contacts) == 0:
            print("\nNo disponemos de ningún contacto guardado.")
        else:
            pass


    elif action == "4":
        if len(contacts) == 0:
            print("\nNo disponemos de ningún contacto guardado.")
        else:
            pass


    elif action == "5":
        break
    
    else:
        print("\nDebe introducir un número del 1 al 5")
    













"""
def search():
    '''Función para búsqueda de contactos y su guardado si es nuevo'''
    search_name = input("Introduce el contacto que estás buscando")
    if search_name in contacts.keys():
        print("Ya guardaste ese contacto")
        print(f("\nEn número de teléfono de {contacts.keys} es {contacts.value}"))
    else:
        print("No se encontró el contacto")
        print("¿Desea guardar el nuevo contacto?")
        response = input("si / no").lower
        if response == "si":
            new_search_numb = int(input("Introduzca el número del nuevo contacto"))
            if len(new_search_numb) < 11 and type(new_search_numb) == int:
                contacts[response] = new_search_numb
                print(f("\nEl nuevo contacto {contacts.keys} tiene el número {contacts.value}"))
        else:
            print("El número de teléfono debe tener menos de 11 cifras y solo admite números")

        

def add_contacts():
    '''Función para añadir un contacto'''
    add_name = input("Introduce el nombre del contacto").lower
    if add_name in contacts.keys():
        print("Ese contacto ya está registrado")
        print(f("\nEn número de teléfono de {contacts.keys} es {contacts.value}"))
    else:
        add_numb = int(input("Introduce el número de teléfono"))
        if len(add_numb) < 11 and type(add_numb) == int:
            contacts[add_name] = add_numb
            print(f("\nEl nuevo contacto {contacts.keys} tiene el número {contacts.value}"))
        else:
            print("El número de teléfono debe tener menos de 11 cifras y solo adminte números")


def update_contacts():
    '''Esta función actualiza un contacto'''

"""