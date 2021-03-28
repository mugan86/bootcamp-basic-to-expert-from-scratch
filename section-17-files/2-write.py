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
        f.write("{}\n".format(input_value) )
    else:
        input_values = False
        print("Dejamos de añadir información por escribir 'exit'")
f.close()

file_path = f"{script_directory}/2-a.txt"
f = open(file_path, "x") 
print("final")