"""
Realizar un programa que imprima en pantalla los números del 1 al 100 (incluido).
Lo haremos con las diferentes opciones
* while
* for (usando “range”)
"""

# while
print("======================while======================")
i = 1

while i <= 100:
    print(i)
    i += 1

# for
print("======================for======================")
for value in range(1, 101):
    print(value)
