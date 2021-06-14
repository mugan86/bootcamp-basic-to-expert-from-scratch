# Primera parte

# Con constructor

set_values = set(("Macarrones", "Merluza", "Bloc de notas",
           "Pechugas de pollo",
           "Ordenador portátil",
           "Auriculares"))
print(set_values)
print(type(set_values))

# Sin constructor

set_values = {"Macarrones", "Merluza", "Bloc de notas",
           "Pechugas de pollo",
           "Ordenador portátil",
           "Auriculares"}
print(set_values)
print(type(set_values))

# Apartado extra

new_set = set()
while True:
    input_value = input("Introduzca un valor. Para salir 'EXIT': ")
    if (input_value == 'EXIT'): break
    new_set.add(input_value)
print(new_set)
print(type(new_set))
