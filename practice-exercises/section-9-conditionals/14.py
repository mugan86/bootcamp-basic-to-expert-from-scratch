"""
Crear un programa que determine el mayor de 3 números DIFERENTES 
introducidos por teclado (float o int, podéis decidir).
Introduce primer número: 18
Introduce segundo número: -1
Introduce tercer número: 36
Resultado esperado: El número con valor mayor es 36.
"""

number_one = int(input("Introduce primer número: "))
number_two = int(input("Introduce segundo número: "))
number_three = int(input("Introduce tercer número: "))

if (number_one == number_two or number_two == number_three
        or number_one == number_three):
    print("El requisito del programa exigía introducir números DIFERENTES")
elif(number_one > number_two and number_one > number_three):
    print(f"El primer valor es el mayor: {number_one}")
elif(number_one < number_two and number_two > number_three):
    print(f"El segundo valor es el mayor: {number_two}")
else:
    print(f"El tercer valor es el mayor: {number_three}")
