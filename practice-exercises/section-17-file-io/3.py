
import os

def print_n_lines(file_name, number_of_lines):
    
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        txt = open(file_path)

        for i in range(number_of_lines):
            line = txt.readline()
            print(line.strip())
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
    except Exception as except_message:
        print(except_message)

print_n_lines('exercise2-3', 3)