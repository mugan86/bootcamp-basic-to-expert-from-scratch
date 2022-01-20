"""
variable_valor = <valor si cumple> <condicion> <valor si no cumple>
"""
"""
if number_value % 2 != 0:
    msg = "Impar" 
else:
    msg = "Par"
"""
number_value = int(input("Introduce un número"))

msg = "Impar" if number_value % 2 != 0 else "Par"

print("El número introducido que es {1} es {0}".format(msg, number_value))


"""
Operador ternario compuesto => equivalente if anidado
if number_value % 2 != 0:
    if number_value == 3:
        msg = "Es igual a 3 y es impar"
    else:
        msg = "Impar"
else:
    msg = "Par"
"""
number_value = int(input("Introduce un número"))

msg = ("Es igual a 3 y es impar" 
if number_value == 3 else "Impar") if number_value % 2 != 0 else "Par"

print("El número introducido que es {1} es {0}".format(msg, number_value))
