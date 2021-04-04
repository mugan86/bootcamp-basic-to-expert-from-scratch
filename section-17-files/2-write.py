import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/2.txt"

f = open(file_path, "w")
# a = Añadir información a la anterior
# w = sobrescribir toda la información
input_values = True
while(input_values):
    input_value = input("Texto a almacenar: ")
    if (input_value != "exit"):
        f.write("{}\n".format(input_value))
    else:
        input_values = False
        print("Dejamos de añadir información por escribir 'exit'")
f.close()

file_path = f"{script_directory}/2-a.txt"
try:
    # Comprobando si existe el path del fichero
    if os.path.exists(file_path):  # EXISTE
        # excepción
        raise FileExistsError("{} ya existe y no se puede crear"
                              .format(file_path))
    else:
        f = open(file_path, "x")
        print("{} creado correctamente".format(file_path))
except FileExistsError as file_exist_error:
    print("Fichero existente: {}".format(file_exist_error))


print("final")
