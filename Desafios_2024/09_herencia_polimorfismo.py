# Herencia y Polimorfismo

"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
# Superclase
class Animal:
    def __init__(self, name : str):
        self.name = name

    def sound(self):
        print(f"{self.name} emite un sonido genérico.")

# Clases heredadas / Subclases
class Perro(Animal):

    def sound(self):
        print(f"{self.name} dice: Guau, Guau.")

class Gato(Animal):

    def sound(self):
        print(f"{self.name} dice: Miau, Miau.")


def print_sound(animal : Animal):   # Función de polimorfismo
    animal.sound()

animal = Animal('Luna')
animal.sound()
print_sound(animal)

perro = Perro('Pluto')
perro.sound()
print_sound(perro)

gato = Gato('Azrael')
gato.sound()
print_sound(gato)

print('########################')

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Empleado:
    def __init__(self, identificador : int, nombre : str):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []

    def añadir(self, empleado):
        self.empleados.append(empleado)

    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)


class Gerente(Empleado):
    
    def coordinar_proyectos(self):
        print(f"El gerente {self.nombre} gestiona todos los proyectos de la empresa.")


class GerenteDeProyecto(Empleado):
    def __init__(self, identificador, nombre, proyecto : str):
        super().__init__(identificador, nombre)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f"El Gerente de Proyecto {self.nombre} coordina \nel proyecto {self.proyecto}.")


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje : str):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def codigo(self):
        print(f"El Programador {self.nombre} está programando en {self.lenguaje}.")

    def añadir(self, empleado : Empleado):
        print(f"Un programador no tiene empleados a su cargo.\n{empleado.nombre} no se añadirá.")




gerente = Gerente(1, 'Luis Rodríguez')
gerente_de_proyecto = GerenteDeProyecto(2, 'Ramón Fernandez', 'web bar Antoñito')
gerente_de_proyecto2 = GerenteDeProyecto(3, 'Virginia Martinez', 'Aplicación móvil Banco')
programador = Programador(8, 'Martín Sanchez', ['Python', 'Java'])
programador2 = Programador(9, 'Luisa Chicote', ['JavaScript', 'Pithon', 'C#'])
programador3 = Programador(11, 'Megan Chicote', ['Java', 'Pithon', 'C#'])
programador4 = Programador(21, 'Leonardo Dantés', ['Kobol', 'C++', 'C#'])

gerente.añadir(gerente_de_proyecto)
gerente.añadir(gerente_de_proyecto2)

gerente_de_proyecto.añadir(programador)
gerente_de_proyecto.añadir(programador2)
gerente_de_proyecto2.añadir(programador3)
gerente_de_proyecto2.añadir(programador4)

programador2.añadir(programador3)

programador.codigo()
programador3.codigo()

gerente.coordinar_proyectos()
gerente_de_proyecto.coordinar_proyecto()
gerente_de_proyecto2.coordinar_proyecto()

gerente.print_empleados()
gerente_de_proyecto.print_empleados()
gerente_de_proyecto2.print_empleados()
programador2.print_empleados()