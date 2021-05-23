"""
Crear un programa con un menú de una calculadora donde tendremos las 
opciones de suma, resta, multiplicación, división, resto (módulo) y salir. 
Introducimos dos números desde consola:
    1.- Suma.
    2.- Resta.
    3.- Multiplicación
    4.- División.
    5.- Resto
    6.- Salir
"""

print("============MINICALCULADORA============")
print("1) Suma")
print("2) Resta")
print("3) Multiplicación")
print("4) División")
print("5) Resto (Módulo)")
print("6) Salir")
print("========================")

option = input("Seleccione operación a realizar:\n")
one_number, second_number = 0, 0
if (option == "1" or option == "2" or option == "3" or option == "4" or option == "5"):
    one_number = float(input("Primer número:\n"))
    second_number = float(input("Segundo número:\n"))
    if (option == "1"):
        print("Has seleccionado realizar una SUMA")
        print(f"{one_number} + {second_number} = {(one_number + second_number)}")
    elif (option == "2"):	
        print("Has seleccionado realizar una RESTA")
        print(f"{one_number} - {second_number} = {(one_number - second_number)}")
    elif (option == "3"):	
        print("Has seleccionado realizar una MULTIPLICACIÓN")
        print(f"{one_number} * {second_number} = {(one_number * second_number)}")
    elif (option == "4"):	
        print("Has seleccionado realizar una DIVISIÓN")
        print(f"{one_number} / {second_number} = {(one_number / second_number)}")
    elif (option == "5"):	
        print("Has seleccionado realizar una RESTO")
        print(f"{one_number} % {second_number} = {(one_number % second_number)}")
elif(option == "6"):
    print("Salir")
else:
    print("Opcion incorrecta.")
