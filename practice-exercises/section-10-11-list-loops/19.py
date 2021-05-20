"""
Crear un programa en el que introducimos números enteros
para comprobar si son primos o no.
Mientras introduzcamos números mayores a 0 y enteros, podremos
ir viendo el resultado si el número introducido es primo / no primo
"""
while True:
    number_value = int(input("Introduce número: "))
    if (number_value < 0):
        break
    for index in range(2, number_value):
        if(number_value % index == 0): 
            print(f"{number_value} no es número primo")
            break
    else:
        print(f"{number_value} ES número primo")
            


