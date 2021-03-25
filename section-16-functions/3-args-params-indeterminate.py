# Por posición 

def max (*values):
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

print("Final")