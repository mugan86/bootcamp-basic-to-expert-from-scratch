from greet import hello
from people import teachers, students as students_list
import califications as cali

print(hello("Anartz"))
print(hello("Mikel"))
# Mostramos los profesores
print("=================PROFESORES===============")
for teacher in teachers:
    print(teacher)
# Mostramos los alumnos/ alumnas
print("=================CALIFICACIONES===============")
for student in students_list:
    print("============{}============".format(student['name']))
    print("{} => ¿Aprobado? {}".format(
        student['calification'],
        cali.pass_course(student['calification'])
    ))