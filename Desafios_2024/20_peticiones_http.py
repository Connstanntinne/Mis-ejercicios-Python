### Peticiones HTTP
"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
"""
import requests
import json

url = "https://chguv.san.gva.es/inicio/"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Se ha producido un erro tipo {response.status_code}")

print("----------------------------")
print(response)
print("----------------------------")
print(response.url)
print("----------------------------")
print(response.encoding)
print("----------------------------")
print(response.status_code)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""

pokemon = input("Indroduce el nombre o id del pokemon a buscar: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Id: {data['id']}")
    print(f"Peso: {data['weight']}")
    print(f"Altura: {data['height']}")
    print(f"Tipo(s): ")
    for type in data['types']:
        print(type['type']['name'])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
    if response.status_code == 200:
        url = response.json()['evolution_chain']['url']

        response = requests.get(url)
        if response.status_code == 200:
            data_chain = response.json()
            print("Cadena de evolución:")

            def get_evolves(data_chain):    #función recursiva ojo!!!
                print(data_chain['species']['name'])
                if 'evolves_to' in data_chain:
                    for evolve in data_chain['evolves_to']:
                        get_evolves(evolve)
            
            get_evolves(data_chain['chain'])


        else:
            print(f"Error: {response.status_code} oteniendo las evoluciones. ")

    else:
        print(f"Error: {response.status_code} obteniendo las evoluciones.")

    print("Juegos en los que aparece:")
    for game in data['game_indices']:
        print(game['version']['name'])

else:
    print(f"Error: {response.status_code} obteniendo las evoluciones.")



