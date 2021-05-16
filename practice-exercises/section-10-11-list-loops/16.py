"""
Escribir un programa, donde añadamos una lista con valores enteros, 
hagamos un backup de ella (clonando o copiando su contenido) en una nueva 
lista llamada “backup”.
Una vez realizado el backup, modificamos los valores de la 
lista original duplicando los valores de cada elemento.
Comprobamos que las listas no son iguales

"""

number_list = [2, 3, 6, 8, 10]
backup = number_list.copy()

print(f"Original: {number_list}")
print(f"Copia: {backup}")
print(f"¿Iguales?: {number_list == backup}")

for number in range(len(number_list)):
    number_list[number] *= 2

print(f"Original: {number_list}")
print(f"Copia: {backup}")
print(f"¿Iguales?: {number_list == backup}")
