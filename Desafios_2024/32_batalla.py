### Batalla Deadpool y Wolverine.
"""
* EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
"""
from abc import ABC, abstractmethod
import random
import time
import sys


class Personaje(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def evade(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def loose(self):
        pass


class Deadpool(Personaje):

    def __init__(self):
        self.life = 500
        self.max_attack = 100

    def attack(self):
        damage = random.randint(10, self.max_attack)
        print(f"Deadpool ha realizado un ataque de {damage}.")
        return damage
    
    def evade(self):
        evade = random.randint(1, 5)
        if evade == 1:
            print("Deadpool consiguió evadir el ataque")
            return True

        else:
            print("Deadpool no consiguió evadir el ataque.")
            return False

    def damage(self, attack: int):
        self.life -= attack
        print(f"Vida actual de Deadpool: {self.life}")

    def loose(self):
        if self.life <= 0:
            print("Deadpool ha perdido el combate.")
            return exit()
        

class Wolverine(Personaje):

    def __init__(self):
        self.life = 500
        self.max_attack = 120

    def attack(self):
        damage = random.randint(10, self.max_attack)
        print(f"Wolverine ha realizado un ataque de {damage}.")
        return damage
    
    def evade(self):
        evade = random.randint(1, 4)
        if evade == 1:
            print("Wolverine consiguió evadir el ataque")
            return True

        else:
            print("Wolverine no consiguió evadir el ataque.")
            return False

    def damage(self, attack: int):
        self.life -= attack
        print(f"Vida actual de Wolverine: {self.life}")

    def loose(self):
        if self.life <= 0:
            print("Wolverine ha perdido el combate.")
            return exit()


deadpool = Deadpool()
wolverine = Wolverine()



def combat(fighter1, fighter2):
    turn = 1
    print(f"Va ha iniciarse el combate entre {fighter1} y {fighter2}.")
    while fighter1.life > 0 and fighter2.life > 0:
        
        print(f"Turno {turn}")
        damage = fighter1.attack()
        evade = fighter2.evade()

        if evade == False:

            if damage == fighter1.max_attack:
                fighter2.damage(damage)
                fighter2.loose()
                fighter1.attack()
                fighter2.evade()

            else:
                fighter2.damage(damage)
                fighter2.loose()


        damage2 = fighter2.attack()
        evade2 = fighter1.evade()

        if evade2 == False:

            if damage2 == fighter1.max_attack:
                fighter1.damage(damage2)
                fighter1.loose()
                fighter2.attack()
                fighter1.evade()

            else:
                fighter1.damage(damage2)
                fighter1.loose()

        time.sleep(1)
        turn += 1



combat(deadpool, wolverine)


