"""
Desarrollar un programa que permita calcular el sueldo mensual de "n" 
empleados de una empresa.  
Especificamos la cantidad de trabajadores desde teclado
(evidentemente tiene que ser 1 ó más.
Una vez ingresado, iteramos añadiendo los siguientes datos por 
trabajador: nombre, categoría y número horas trabajadas. 
Si la categoría es A, el pago por hora es de 50 dólares, si es B 
es de 80 dólares, si es C es de 90 dólares y si es D es de 120 dólares. 
Si no se introduce correctamente la categoría, el pag o es de 35 dólares. 
Mostrar el pago que le corresponde a cada trabajador, el pago total 
que se debe hacer, el total de trabajadores que ganan menos de 5000 
dólares, el total que ganan desde 5000 dólares a 9000 dólares y los 
que ganan más de 9000 dólares.
Toda esta información, para no perderla, la guardaremos en un 
fichero de texto línea a línea, por lo que todo los resutados que 
se han ido mostrando, han tenido que ser almacenados en una lista 
para después ir almacenándolo.
"""
import os

employees_list = []
categories_salary = {
    'A': 50,
    'B': 80,
    'C': 90,
    'D': 120
}
# 1.- Introducir número de empleados con validación
while True:
    try:
        people_work = int(input("Introduzca número de empleados: "))
        if (people_work > 0):
            break
        else:
            print("Debes de introducir un número superior a 0")
    except ValueError as value_error_message:
        print("Debes de introducir un número entero")

# 2.- Introducir datos de los empleados y asignar datos

for i in range(people_work):
    # nombre, categoría y número horas trabajadas.
    employee = dict()
    employee['name'] = input("Introduce nombre / apellidos: ")
    employee['category'] = input("Introduce categoría A, B, C, D: ").upper()
    # Asignar el salario / hora por la categoría
    if (employee['category'] in categories_salary):
        employee['salary_per_hour'] = categories_salary[employee['category']]
    else: 
        employee['salary_per_hour'] = 35
    # Validamos la entrada de las horas, forzando a que sea nº enteros
    while True:
        try:
            employee['hours_work'] = int(input("Introduce horas trabajadas: "))
            break
        except ValueError:
            print("Hay que introducir bien las horas de trabajo. Números enteros")
    employee['salary'] = employee['salary_per_hour'] * employee['hours_work']
    employees_list.append(employee)

# 3.- Clasificar los trabajadores por los rangos de sueldo

"""
< 5000
5000 <= sueldo <= 9000
> 9000
"""
salary_ranking_employees = {
    'under_5000': [],
    '5000-9000': [],
    'over_9000': []
}
for employee in employees_list:
    
    if (employee['salary'] < 5000): 
        salary_ranking_employees['under_5000'].append(employee)
    elif (5000 <= employee['salary'] <= 9000): 
        salary_ranking_employees['5000-9000'].append(employee)
    else:
        salary_ranking_employees['over_9000'].append(employee)

# 4- Guardar los cambios en los ficheros
try:
    # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
    script_directory = os.path.dirname(__file__)
    file_path = f"{script_directory}/employees.txt"
    txt = open(file_path, "w")
    txt.write(f"name,category,salary_per_hour,hours_work,salary\n")
    for employee_item in employees_list:
        text_data = f"{employee_item['name']}," + \
                    f"{employee_item['category']}," + \
                    f"{employee_item['salary_per_hour']}," + \
                    f"{employee_item['hours_work']}," + \
                    f"{employee_item['salary']}"
        txt.write(f"{text_data}\n")
    txt.close()
    file_path = f"{script_directory}/employees_ranking_salaries.txt"
    txt = open(file_path, "w")
    # Items completo
    for key_value, value in salary_ranking_employees.items():
        txt.write("===========================\n")
        txt.write(f"\t{key_value}\n")
        txt.write("===========================\n")
        print(f"{key_value}:     \t{value}")
        for employee_value in value:
            text_data = f"{employee_value['name']}," + \
                        f"{employee_value['category']}," + \
                        f"{employee_value['salary_per_hour']}," + \
                        f"{employee_value['hours_work']}," + \
                        f"{employee_value['salary']}"
            txt.write(f"{text_data}\n")
    txt.close()
except FileExistsError:
    print("Fichero existe")
except Exception as except_message:
    print(except_message)
