
# Ejercicios Clases

"""
# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
"""

# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y 
# un método "make_sound" que imprima un sonido genérico.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Sonido genérico")

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y 
# almacénala en una propiedad pública. Añade el método "make_sound" que 
# imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self, species, sound = "Sonido genérico"):
        self.species = species

    def make_sound(self):
        if self.species == 'dog':
            print('GuauGuau')
        elif self.species == 'cat':
            print('Miaumiau')
        else:
            print("Sonido genérico")

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". 
# Además, debe tener una propiedad privada "_speed" que inicialmente será 0.

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
        self._speed = 0

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad
# en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades.
# Asegúrate de que la velocidad no sea negativa.

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
        self._speed = 0

    def accelerate(self):
        self._speed += 10

    def brake(self):
        self._speed = max(0, self._speed - 10)


# 5. Crea una clase "Book" que tenga propiedades como "title" (púlico) y "author" (privado). 
# Añade un método para obtener el autor y otro para cambiar el tí­tulo del libro.

class Book:
    def __init__(self, title, author):
        self.title = title
        self._author = author

    def take_author(self):
        return self._author

    def change_title(self, new_title):
        self.title = new_title

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. 
# Añade un método para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, nombre : str, apellido : str, notas : int):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def nota_media(self):
        return sum(self.notas) / len(self.notas)


# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". 
# Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar
# más de lo que hay en la cuenta.

class BamkAccount:
    def __init__(self, owner : str, balance: int):
        self.owner = owner
        self.balance = balance

    def depositar(self, amount):
        self.balance += amount

    def retirar(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("No dispone de esa cantidad a retirar en su cuenta.")


# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". 
# Añade un método que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x, y):      # mia
        self.x = x
        self.y = y

    def distance(self, x1, y1):
        return ((abs(x1 - self.x))**2 + (abs(y1 - self.y))**2)**0.5   # para no importar módulos



class Point:
    def __init__(self, x, y):            # Moure
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5


# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora)
# y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def salary(self):
        return self.hourly_wage * self.hours_worked


# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). 
# Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self):
        self.inventory = []

    def add_inventory(self, new_item):
        self.inventory.append(new_item)

    def show_inventory(self):
        print(self.inventory)

        for items in self.inventory:
            print(items)

