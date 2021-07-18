import os

# Parte 1 - Introducir el número de alumnos/as y nombre del curso
print("=======================================================================")
print("Gestión de notas - \"Anartz Mugika Ledo - Desarrollo / Formación\"")
print("=======================================================================")
print("\n\t\t\tDATOS GENERALES")
print("=======================================================================")

while True:
    try:
        number_students = int(input("Introduce número de alumnos/as: "))
    except ValueError:
        number_students = 0
    except Exception as message:
        print("Error: " + message)
    if (number_students > 0):
        break
    else:
        print("Debes de introducir un número superior a 0")

while True:
    course_name = input("Introduzca el nombre del curso: ")
    if (course_name != '' and course_name != None):
        break

print("-----------------------------------------------------------------------")
print(
    f"Número de alumnos/as: {number_students} / Nombre del curso: {course_name}")

# Parte 2 - Introducir la información de los/as alumnos/as
print("=======================================================================")
print("\n\t\t\tInformación de los/as alumnos/as")
print("=======================================================================")
students_data = []
calification_acumulator = 0
for i in range(number_students):
    # Introducir información de los estudiantes
    print(f"Datos de estudiante - {i +  1}")
    # Añadimos el while para controlar que introducimos algo
    while True:
        name_lastname = input("Introduzca nombre y apellidos: ")
        if (name_lastname != '' and name_lastname != None):
            break
    while True:
        email = input("Introduzca email: ")
        if (email != '' and email != None):
            break
    while True:
        try:
            calification = float(
                input("Introduce nota (de 0 a 10 incluidos): "))
        except ValueError:
            calification = -1
        except Exception as message:
            print("Error: " + message)
        if (calification >= 0 and calification <= 10):
            calification_acumulator += calification
            break
        else:
            print("Debes de introducir una nota válida de 0 a 10 (incluido)")
    students_data.append(dict(name_lastname=name_lastname,
                              email=email, calification=calification))
    print("-----------------------------------------------------------------------")

# Parte 3.- <suma notas de todos estudiantes> / <nº estudiantes> = NOTA MEDIA
avg_calification = calification_acumulator / number_students
print(f"Nota media de la clase: {avg_calification}")

# Parte 4.- Clasificar alumnos/as con nota superioresa la media y por debajo
above_avg = []
below_avg = []
for value in students_data:
    calification = value['calification']
    if (calification >= avg_calification):
        above_avg.append(value)
    else:
        below_avg.append(value)

# 5.- Almacenar la información
try:
    # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
    script_directory = os.path.dirname(__file__)
    # 5.1.- students.txt
    file_path = f"{script_directory}/students.txt"
    txt = open(file_path, "w")
    txt.write("===========================\n")
    txt.write(f"Notas de {course_name}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in students_data:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.write("===========================\n")
    txt.write(f"PROMEDIO DE LA CLASE: {avg_calification:.2f}\n")
    txt.write("===========================\n")
    txt.close()
    # 5.2.- Alumnos por debajo de la media y por encima
    file_path = f"{script_directory}/report-students-avg-data.txt"
    txt = open(file_path, "w")
    txt.write("===========================\n")
    txt.write(f"Notas de {course_name} superiores a la media: \
                {avg_calification}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in above_avg:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.write("===========================\n")
    txt.write(f"Notas de {course_name} inferiores a la media: \
    {avg_calification}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in below_avg:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.close()
except FileExistsError:
    print("Fichero existe")
except Exception as except_message:
    print(except_message)
