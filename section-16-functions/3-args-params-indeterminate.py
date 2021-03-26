# Por posición

def max(*values):
    # Asignar el primer valor como el máximo
    max_value = values[0] if len(values) > 0 else None

    if max_value != None:
        for value in values:
            if max_value < value:
                max_value = value
        print("El valor máximo de {} es {}".format(values, max_value))
    else:
        print("No existen valores y no hay máximo")


# Probando por posición
print("Por posición")
max(12, 3, 456, 457, 1090, 3456)
max(-12, 3, 7890, -4587, 1090, 3456)

# Por nombre


def personal_info_show(**person_info):
    try:
        if (len(person_info) == 0):
            raise ValueError("Necesitamos algo de información")
        for key, value in person_info.items():
            print("{} => {}".format(key, value))
    except ValueError as value_error_message:
        print(value_error_message)
    except Exception as exception:
        print("Excepción general:")
        print(exception)


# Llamamos a la función y pasamos información
personal_info_show(name="Anartz", lastname="Mugika", age=35)
personal_info_show()

# Por posición y por nombre


def class_avg_califications(*califications, **students):
    try:
        # Comprobar si el número de notas / alumnos/as es diferente
        if (len(califications) != len(students)):
            raise ValueError("Debemos de especificar el mismo número" +
                            " de nota y alumnos/as")
        # Contar calificaciones y sacar media
        total = 0
        for calification in califications:
            total += calification
        print("Nota media: {}".format(total / len(califications)))

        # Mostrar lista de estudiantes
        for key, value in students.items():
            print("{} => {}".format(key, value))
    except ValueError as value_error_message:
        print(value_error_message)
    


class_avg_califications(9.5, 4.5, student_one="Anartz",
                        student_two="Mikel")
class_avg_califications(9.5, 4.5, 4.5, student_one="Anartz",
                        student_two="Mikel")
print("Final")
