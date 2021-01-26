"""
Tenemos que tener en cuenta:
Tenemos dos partes: real e imaginaria
Positivo / negativo
CON / SIN decimales
Ilimitado
Podemos mostrar con un guión bajo para leer mejor los miles
Podemos trabajar con números cientificos
"""
x = 34 + 56j
y = -34.45 + 56.56j
z = -34.45 - 56.56j

print(type(x))
print(type(y))
print(type(z))
print("Real: " + str(z.real) + " / Imaginario: " + str(z.imag))
print("Final del programa")