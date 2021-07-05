"""
Crear un programa que lea un fichero línea a línea y a su vez vaya 
almacenando esta información en una lista (Podemos usar el de 
cualquier ejercicio anterior) para mostrar 
todo el contenido de golpe con un print al finalizar el programa
"""

import os
file_name = "exercise4"
def get_filelines_content():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        return open(file_path).readlines()
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
        return []
    except Exception as except_message:
        print(except_message)
        return []

print(get_filelines_content())