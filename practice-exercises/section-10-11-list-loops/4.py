"""
Realizar un programa que imprima en pantalla los números del 100 al 1.
Lo haremos con las diferentes opciones
* while
* for (usando “range”)
"""

# while
print("======================while (descontar)======================")
i = 100

while i >= 1:
    print(i)
    i -= 1

# for
print("======================for (descontar)======================")
for value in range(100, 0, -1):
    print(value)