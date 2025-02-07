### Desafio 31: Simulador de Juegos Olímpicos.

import random


class Participant:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self):
        return hash(self.name, self.country)



class Olympics:
    def __init__(self):
        self.events = []
        self.participants = dict() 
        self.results = dict()
        self.country_results = dict()

    def event_reg(self):
        new_event = input("Introduzca un evento: ").strip()

        if new_event in self.events:
            print(f"El evento {new_event} ya ha sido registrado.")
        else:
            self.events.append(new_event)
            print(f"El evento {new_event} se ha registrado correctamente.")

    def participant_reg(self):

        if not self.events:
            print("No existen eventos registrados.")
            return

        name = input("Introduce el nombre del participante: ").strip()
        country = input("Introduce el país del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos disponibles: ")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choice = int(input("Seleccione un evento para el participante: ")) - 1
        
        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]

            if event in self.participants and participant in self.participants[event]:
                print(f"El participante {participant} ya está registrado en el evento {event}.")
                
            else:
                if event not in self.participants:
                    self.participants[event] = []

                self.participants[event].append(participant)
                print(f"El participante {name} de {country} se ha registrado en {event}.")

        else:
            print("Selección de evento deportivo inválida. El participante no se ha registrado.")

    def simulate_event(self):
        if not self.events:
            print("No existen eventos registrados.")
            return

        for event in self.events:

            if len(self.participants[event]) < 3:
                print(f"No existen suficientes participantes para el evento {event}. Deben ser al menos 3.")
                continue

            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            self.results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultado de simulación del evento: {event}")
            print(f"Oro: {gold.name}({gold.country})")
            print(f"Plata: {silver.name}({silver.country})")
            print(f"Bronce: {bronze.name}({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {
                "gold": 0, "silver": 0, "bronze": 0}

        self.country_results[country][medal] += 1

    def show_report(self):

        print("Informe de los Juegos Olímpicos:")
        if self.results:
            print("Informe de eventos: ")

            for event, winner in self.results.items():
                print(f"Evento: {event}")
                print(f"Oro: {winner[0].name}({winner[0].country})")
                print(f"Plata: {winner[1].name}({winner[1].country})")
                print(f"Bronce: {winner[2].name}({winner[2].country})")

        else:
            print("No hay eventos registrados.")

        print()

        if self.country_results:

            print("Informe por país: ")

            for country, medals in sorted(self.country_results.items(), key = lambda x:(x[1]['gold'], x[1]['silver'], x[1]['bronze']), reverse=True):

                print(f"{country}: Oro {medals['gold']}, Plata {medals['silver']}, Bronce {medals['bronze']} ] ")
        else:
            print("No hay medallas registradas.")





olympics = Olympics()
print("Este es un simulador de los Juegos Olímpicos.")

while True:

    print("\nElija una opción válida.")
    print("1. Registro de evento deportivo.")
    print("2. Registro de participantes.")
    print("3. Simulación de eventos.")
    print("4. Creación de informes.")
    print("5. Salir.")

    
    option = input("Seleccione una opción: ")
    match option:
        case "1":
            olympics.event_reg()
        case "2":
            olympics.participant_reg()
        case "3":
            olympics.simulate_event()
        case "4":
            olympics.show_report()
        case "5":
            print("Saliendo de la aplicación...")
            break
        case _:
            print("Opción no válida. Debe seleccionar un número del 1-5.")










