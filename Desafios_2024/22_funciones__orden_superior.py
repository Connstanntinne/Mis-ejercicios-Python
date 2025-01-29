### Funciones de orden superior
"""
EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""
# funciones que tiene a otras furciones como argumentos y funciones que 
# retornan otras funciones

# función que tiene a otra función como argumento
def sum_one(value):
    return value + 1

def multiply_two_num_and_add_one(num1, num2, f):
    return f(num1 * num2)

print(multiply_two_num_and_add_one(3, 5, sum_one))

# función que retorna otra función
def multiply_two(x):
    def multiply(y):
        return x * y
    return multiply

print(multiply_two(2)(3))
double = multiply_two(2)
print(double(5))

# funciones superiores 'built-in' del sistema
lista = [3, 5, 6, 24, 52]

def double_num(n1):
    return n1 * 2

print(list(map(double_num, lista)))
print(list(map(lambda n: n * 2, lista)))


"""
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""

students = [
    ['Dani', '21/02/2009', [8, 10, 9, 7, 8]], 
    ['Juan', '12/09/2009', [9, 10, 9, 10, 8]], 
    ['Roberto', '01/05/2009', [8, 7, 9, 10, 8]], 
    ['Sara', '23/11/2008', [8, 10, 9, 9, 9]]
]

print(students[1])

def mean_note():
    ''' calcular la nota media de cada estudiante y generar lista'''
    mean_list = []
    for student in students:
        mean = sum(student[2]) / len(student[2])
        mean_list.append(mean)
    return  mean_list

print(list(mean_note()))


def students_list():
    '''generar lista de los nombres'''
    name_list = []
    for student in students:
        name_list.append(student[0])
    return name_list

# Promedio calificaciones: Obtiene una lista de estudiantes por nombre
# y promedio de sus calificaciones

def students_main_list(f1, f2):
    '''generador de diccionario nombre-nota media'''
    mean_list = f1()
    name_list = f2()
    new_list = (dict(zip(name_list, mean_list)))
    print(new_list)

    for name, note in new_list.items():
        print(f"El estudiante {name} ha obtenido una notamedia de {note}")
        

students_main_list(mean_note, students_list)

# Mejores estudiantes

def better_students(f1, f2):
    '''buscar a los estudiantes con notas >= 9'''
    mean_list = f1()
    name_list = f2()
    new_list = (dict(zip(name_list, mean_list)))
    print(new_list)
    print('Los mejores estudiantes han sido: ')

    for name, note in new_list.items():
        if note >= 9:
            print(f"El estudiante {name} ha obtenido una notamedia de {note}")

better_students(mean_note, students_list)


# Listado de estudiates por edad

import datetime
from datetime import timedelta


def age():
    '''función para hacer listado por edad de estudiantes'''
    today = datetime.datetime.today()
    print(today)
    birthday_format = []
    birthday = []
    for student in students:
        birthday.append(student[1])

    for d in birthday:
        m = today - datetime.datetime.strptime(d, '%d/%m/%Y')
        birthday_format.append(m)
        
    return birthday_format

def student_age_list(f1, f2):
    '''ordenar estudiantes por edad'''
    name_list = f1()
    birthday_format = f2()
    listed_ages = dict(zip(name_list, birthday_format))
    print(listed_ages)
    sorted_listed_ages = dict(sorted(listed_ages.items(), key=lambda item: item[1]))
    print(sorted_listed_ages)
    print(f'El orden de los estudiantes por edad, de menor a mayor es : {list(sorted_listed_ages.keys())}')

student_age_list(students_list, age)


# Mayor calificación

def higher_calification(f1, f2):
    mean_list = f1()
    name_list = f2()
    new_list = (dict(zip(name_list, mean_list)))
    sorted_new_list = dict(sorted(new_list.items(), key=lambda item: item[1]))
    print(f"El estudiante con mejor nota es {list(sorted_new_list.keys())[-1]} con una nota de {list(sorted_new_list.values())[-1]}")


higher_calification(mean_note, students_list)


# con funciones superiores del sistema
print('---------------------------------')
print('---------------------------------')

students = [
    {"name": "Brais", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "moure", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "mouredev", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate": "25-01-1980",
        "grades": [10, 9, 9.7, 9.9]}
]


def average(grades):
    return sum(grades) / len(grades)

# Promedio


print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)

# Mejores

print(
    list(
        map(lambda student:
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
    )
)

# Fecha de nacimiento ordenada
from datetime import datetime

print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True))

# Califiación más alta

print(max(map(lambda student: max(student["grades"]), students)))