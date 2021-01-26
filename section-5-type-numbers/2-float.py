"""
Tenemos que tener en cuenta:
Positivo / negativo
CON decimales
Ilimitado
Podemos mostrar con un guión bajo para leer mejor los miles
Podemos trabajar con números cientificos
"""
# Básico
x = 2.343
y = -35_483.34
z = 345.3839830900000000000000000000000

# Mostrar el resultado para los humanos
real = 4.04000000000000000000045
real_string = f'{real:.2f}'

# Números cientificos

x = 345.56e3 # 345.56 * 10^3 = 345.56 * 1000 = 345560.0
y = 12e5     # 12 * 10^5 = 12 * 100000 = 1200000.0
z = -877.88e110 # -8.7788e112
print("Final del programa")