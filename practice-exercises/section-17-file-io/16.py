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
    if (number_students > 0): break
    else: print("Debes de introducir un número superior a 0")

while True:
    course_name = input("Introduzca el nombre del curso: ")
    if (course_name != '' and course_name != None) : break

print("-----------------------------------------------------------------------")
print(f"Número de alumnos/as: {number_students} / Nombre del curso: {course_name}")

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
        if (name_lastname != '' and name_lastname != None) : break
    while True:
        email = input("Introduzca email: ")
        if (email != '' and email != None) : break
    while True:
        try: 
            calification = int(input("Introduce nota (de 0 a 10 incluidos): "))
        except ValueError:
            calification = -1
        except Exception as message:
            print("Error: " + message)
        if (calification >= 0 and calification <= 10): 
            calification_acumulator += calification
            break
        else: print("Debes de introducir una nota válida de 0 a 10 (incluido)")
    students_data.append(dict(name_lastname = name_lastname, email = email, calification=calification))
    print("-----------------------------------------------------------------------")

# <suma notas de todos estudiantes> / <nº estudiantes> = NOTA MEDIA
avg_calification = calification_acumulator / number_students
print(f"Nota media de la clase: {avg_calification}")
print(students_data)
    
"""
Teniendo la nota media, contamos las personas que están por encima y las que está por debajo de esa media.
Una vez que tenemos esto, es conveniente tener preparado para guardar esa información en un fichero de texto.
Lo que tendremos que tener al final del ejercicio almacenado, es lo siguiente:
Listado de alumos/as con sus notas y el promediofinal: students.txt
Estudiantes que están por encima de la media y por debajo (en dos bloques) en el fichero report-students-avg-data.txt

"""



