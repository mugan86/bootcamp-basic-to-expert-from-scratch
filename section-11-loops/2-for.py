# for básico
numbers = [6, 5, 3, 5, 3]
total = 0

for number_value in numbers:
    total += number_value   # 6, 11, 14, 19, 22

# resultado => total = 22

# for con "break"
numbers = [6, 5, 3, 5, 3]
total = 0

for number_value in numbers:
    if (total >= 15):
        break
    total += number_value   # 6, 11, 14, 19
# for con "continue"

numbers = [6, 5, 3, 5, 3]
total = 0

for number_value in numbers:
    if (total >= 10):
        continue
    total += number_value   # 6, 11

# range (por defecto - numero de iteraciones => range(numero))
list = ["java", "c#", "python", "javascript"]

for i in range(len(list)):
    value = list[i] # java, c#, python, javascript

# Especifcando la posición inicial  en range
for i in range(1, len(list)):
    value = list[i] # c#, python, javascript

# Especificando el incremento en "range"

# Empezamos en el índice 2, hasta 10 e incrementamos de 2 en 2
# 2, 4, 6, 8

for i in range(2, 10, 2):
    value = i

# Usando else para notificar que se ha finalizado
for i in range(2, 10, 2):
    value = i
else:
    value = "Hemos finalizado el bucle for por llegar a 10"

for i in range(2, 10, 2):
    if (i == 4):
        break
    value = i
else:
    value = "Hemos finalizado el bucle for por llegar a 10"

# Bucle anidado

for i in range(2):
    for j in range(4):
        value = f"Fila: { i + 1} / Columna: { j + 1}"

print("Final ")