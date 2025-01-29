### asincronía

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
"""

import time
import datetime
import asyncio


async def task(name: str, duration: int):

    start= datetime.datetime.now()
    print(f'La función {name} ha comenzado: {start}.')
    
    await asyncio.sleep(duration)
    
    end= datetime.datetime.now()
    elapsed_time= end - start
    print(f'La función {name} ha acabado: {end}.')
    print(f'La función ha durado {elapsed_time} segundos.')

asyncio.run(task('1', 2))


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""


async def async_tasks():
    await asyncio.gather(task('C', 3), task('B', 2), task('C', 1))
    await task('D', 1)

asyncio.run(async_tasks())