import os

# Definimos función para abrir el fichero especificado
def open_print_select_file(file_name):
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        txt = open(file_path)
        print(txt.read())
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
    except Exception as except_message:
        print(except_message)

open_print_select_file('exercise1')