# Sin índice

tuple_elements = ("java", "python", "kotlin", "javascript", "c#")

for element in tuple_elements:
    print(element) # "java", "python", "kotlin", "javascript", "c#"

# Ejecutando "break"
for element in tuple_elements:
    if (element == "kotlin"):
        break
    print(element) # "java", "python"

# Usando el índice

# Básico - núm.iteraciones
for i in range(len(tuple_elements)):
    print(f"[{i}] => {tuple_elements[i]}")

# Seleccionando posición de inicio
for i in range(2, len(tuple_elements)):
    print(f"[{i}] => {tuple_elements[i]}")

# Seleccionando posición de inicio y el incremento
for i in range(0, len(tuple_elements), 2): # 0, 2, 4
    print(f"[{i}] => {tuple_elements[i]}")

print("FINAL DEL PROGRAMA")