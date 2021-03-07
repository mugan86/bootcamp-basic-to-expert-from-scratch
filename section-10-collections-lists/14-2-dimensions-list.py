# Crear lista de 2 dimensiones equivalente a una tabla

students_classroom = [
    #   C1        C2       C3
    ["Anartz", "Mikel", "Aitor"],   # F1 => Fila - 1 = Indice = 0
    ["Maite",  "Miren", "Naiara"],   # F2 => Fila - 1 = Indice = 1
    ["Joxe",   "Aitor", "Mikel"],    # F3 => Fila - 1 = Indice = 2
]

# lista[fila - 1][ columna - 1]

# Alumnos seleccionados individualmente
student = students_classroom[0][0] # Anartz
student = students_classroom[0][1] # Mikel
student = students_classroom[0][2] # Aitor

student = students_classroom[1][1] # Miren

student = students_classroom[2][2] # Mikel el de debajo de la esquina

# Modificar información

students_classroom[0][2] = "Amaia" # Aitor => Amaia

students_classroom[1][1] = "Miren Miren" # Miren => Miren Miren

students_classroom[2][2] = "Mikel Mikel Mikel" # Mikel x 3

# Cambiar elementos de una fila completa (Fila 3 )=> Indice 2
students_classroom[2][:] = ["Inaxio", "Mireia", "Alaitz"]
print("********")


