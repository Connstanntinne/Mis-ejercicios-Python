### Fechas

"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""
from datetime import datetime, timedelta

today = datetime.now()
print(today)
my_birthday = datetime(1978, 8, 17, 16, 30)
print(my_birthday)

my_life = (today - my_birthday)
print(my_life)
lived_years = (my_life // timedelta(days=365))
print(lived_years)



"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""

my_birthday = datetime(1978, 8, 17, 16, 30)
print(my_birthday.strftime('%d/%m/%Y'))
print(my_birthday.strftime('%H:%M:%S'))
print(my_birthday.strftime('%j'))
print(my_birthday.strftime('%A'))
print(my_birthday.strftime('%B'))
print(my_birthday.strftime('%c'))
print(my_birthday.strftime('%x'))
print(my_birthday.strftime('%X'))
print(my_birthday.strftime('%A %B %H:%M:%S'))

print(today.strftime('%H:%M:%S'))
print(today.strftime('%d/%m/%Y'))








