# Por posición, por nombre, sin argumentos

def max_two_values(first_value = None, second_value = None):
    if ( first_value == None or second_value == None):
        print("Debemos de especificar los dos valores")
        return
    if first_value > second_value:
        print("Primer valor máximo")
    elif first_value < second_value:
        print("Segundo valor máximo")
    else:
        print("Son iguales")

# Por posición 
print("Por posición")
max_two_values(12, 3) # Primer valor máximo
max_two_values(3, 12) # Segundo valor máximo
max_two_values(3, 3)  # Son iguales

# Por nombre 
print("Por nombre")
max_two_values(second_value = 12, first_value = 3) # Segundo valor máximo
max_two_values(second_value = 3, first_value = 12)  # Primer valor máximo
max_two_values(second_value = 3, first_value = 15)  # Primer valor máximo

# Sin argumentos
print("Sin argumentos")
try:
    max_two_values()
except Exception as exception_message:
    print(exception_message)
print("Final")