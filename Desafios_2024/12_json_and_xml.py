### Manejo de ficheros JSON y XML

"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
"""
# .xml
import xml.etree.ElementTree as ET
import os

root = ET.Element("Persona")

atributo1 = ET.SubElement(root,"Nombre", Nombre = "Oscar")
atributo2 = ET.SubElement(root, "Edad", Edad = '46')
atributo3 = ET.SubElement(root, "Fecha_de_nacimeinto", 
                          Fecha_de_nacimiento = "17 de agosto de 1978")
atributo4 = ET.SubElement(root, "Listado_de_lenguajes_de_programación", 
                          Listado = ["Python", "C#"])

tree = ET.ElementTree(root)
my_xml_file= "Desafios_2024/my_xml.xml"
tree.write(my_xml_file, encoding= "utf-8", xml_declaration= True)

print(f"Archivo XML creado: {my_xml_file}")

with open(my_xml_file, 'r') as file:
    #print(file.read())
    for line in file.readlines():
        print(line)

os.remove(my_xml_file)

print('#########################')
# .json

import json

datos = {
    'Nombre' : 'Oscar',
    'Edad' : 46,
    'Fecha de nacimeinto' : '17 de agosto de 1978',
    'Listado de lenguajes de programación': ['Python', 'C#']
}

my_json_file = open('Desafios_2024/my_json.json', 'w')

json.dump(datos, my_json_file, indent=4)

my_json_file.close()

with open('Desafios_2024/my_json.json', 'r') as file:
    for line in file.readlines():
        print(line)

os.remove('Desafios_2024/my_json.json')

print('#########################')

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""


