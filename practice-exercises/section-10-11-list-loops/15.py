"""
Filtrar los valores de una lista que contiene una longitud de 
n caracteres ó más.
n: Valor que especificamos introduciendo desde teclado
"""

# Pedimos el número de caracteres que será para el filtro en el resultado

while True:
    input_value = int(input("Introduce nº caracteres: "))
    if (input_value <= 0):
        print(f"Debes de especificar 1 ó más. {input_value} no es correcto.")
        continue
    break

programming_languages = ["Java", "Javascript", "Go", "Python", "Rust"]

result = []

for language in programming_languages:
    if len(language) >= input_value:
        result.append(language)

print(f"Lista original: {programming_languages}")
print(f"Resultado: {result}")
