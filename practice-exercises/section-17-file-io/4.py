"""Añadir texto línea a línea con una entrada por teclado hasta que 
se introduzca “EXIT”. Cuando ya dejamos de introducir, cerrar el flujo y
posteriormente abrimos ese fichero y hacemos como 
en el ejercicio 1 mostrar todo el contenido después de abrirlo"""

import os
file_name = "exercise4"
def save(input_text):
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        txt = open(file_path, "a")
        txt.write(f"{input_text}\n")
        txt.close()
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
    except Exception as except_message:
        print(except_message)

def input_data_in_file():
    while True:
        input_text = input("Introduce el texto. \"EXIT\" para salir: \n")
        if input_text == "EXIT": break
        save(input_text)

input_data_in_file()
