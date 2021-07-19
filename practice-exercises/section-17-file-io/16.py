import os

def print_head():
    print("=======================================================================")
    print("Gestión de notas - \"Anartz Mugika Ledo - Desarrollo / Formación\"")
    print("=======================================================================")
    print("\n\t\t\tDATOS GENERALES")
    print("=======================================================================")

def start_program():
    print_head()
    # Parte 1 - Introducir el número de alumnos/as y nombre del curso
    number_students, course_name = input_students_course_name()

    print_start_input_info(number_students, course_name)

    students_data, calification_acumulator = add_students_info(number_students)

    avg = calculate_course_average(calification_acumulator, number_students)

    above_avg, below_avg = classified_students_respect_avg(students_data, avg)

    save_data_in_files(course_name, avg, above_avg, below_avg, students_data)

def input_students_course_name():
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
    return (number_students, course_name)

def print_start_input_info(number_students, course_name):
    print("-----------------------------------------------------------------------")
    print(
        f"Número de alumnos/as: {number_students} / Nombre del curso: {course_name}")

def add_students_info(number_students):

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
    return students_data, calification_acumulator

def calculate_course_average(califications, students):
    # Parte 3.- <suma notas de todos estudiantes> / <nº estudiantes> = NOTA MEDIA
    avg_calification = califications / students
    print(f"Nota media de la clase: {avg_calification:.2f}")
    return avg_calification

def classified_students_respect_avg(students, avg):
    # Parte 4.- Clasificar alumnos/as con nota superioresa la media y por debajo
    above_avg = []
    below_avg = []
    for value in students:
        calification = value['calification']
        if (calification >= avg):
            above_avg.append(value)
        else:
            below_avg.append(value)
    return above_avg, below_avg

def save_data_in_files(course, avg, above_avg, below_avg, students): 
    # 5.- Almacenar la información
    try:
    # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        # 5.1.- students.txt
        save_students_principal(script_directory, course, students, avg)
        # 5.2.- Alumnos por debajo de la media y por encima
        save_avg_classfied(script_directory, course, avg, above_avg, below_avg)
    except FileExistsError:
        print("Fichero existe")
    except Exception as except_message:
        print(except_message)

def save_students_principal(directory, course, students, avg):
    file_path = f"{directory}/students.txt"
    txt = open(file_path, "w")
    txt.write("===========================\n")
    txt.write(f"Notas de {course}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in students:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.write("===========================\n")
    txt.write(f"PROMEDIO DE LA CLASE: {avg:.2f}\n")
    txt.write("===========================\n")
    txt.close()

def save_avg_classfied(directory, course, avg, above_avg, below_avg):
    file_path = f"{directory}/report-students-avg-data.txt"
    txt = open(file_path, "w")
    txt.write("===========================\n")
    txt.write(f"Notas de {course} superiores a la media: \
                {avg:.2f}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in above_avg:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.write("===========================\n")
    txt.write(f"Notas de {course} inferiores a la media: \
    {avg:.2f}\n")
    txt.write("===========================\n")
    txt.write(f"Nombre / Apellidos,Correo electrónico,Nota\n")
    for item in below_avg:
        text_data = f"{item['name_lastname']}," + \
                    f"{item['email']}," + \
                    f"{item['calification']}"
        txt.write(f"{text_data}\n")
    txt.close()


start_program()