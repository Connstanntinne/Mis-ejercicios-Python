### Enumeraciones
"""
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
"""
from enum import Enum

week_day = Enum(
    value= 'week_day',
    names= ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 
            'Sábado', 'Domingo')
)

print(week_day.Lunes)
print(week_day.Lunes.value)
print(week_day.Lunes.name)
print(week_day['Lunes'].name)
print(week_day(1).name)
print(repr(week_day.Lunes))
print(week_day.Lunes is not week_day.Martes)
print(week_day.Jueves in week_day)


def day(num: int):
    print(week_day(num).name)
    print(week_day(num))

day(2)
day(5)

print('==========================')

class WeekDay(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def day(num: int):
    print(week_day(num).name)
    print(week_day(num))

day(2)
day(5)



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""

class OrderStatus(Enum):
    PENDING = 0
    SHIPPED = 1
    DELIVERED = 2
    CANCELLED = 3

class Order: 

    status = OrderStatus.PENDING

    def __init__(self, id : int):
        self.id = id

    def shipped(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.print_status()
        else:
            print("El pedido no está pendiente de envio.")

    def delivered(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.print_status()
        else:
            print("El envío debe ser enviado antes de entregarse.")
    def cancelled(self): 
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.print_status()
        else:
            print("El pedido ya no puede ser cancelado porque ha sido entregado.")

    def print_status(self):
        print(f"El pedido {self.id} actualmente se encuentra {self.status.name}.")


order_1 = Order(1)
order_1.print_status()
order_1.delivered()
order_1.print_status()
order_1.shipped()
order_1.delivered()
order_1.cancelled()

