"""
Realizar un programa que imprima en pantalla los números impares del 1 al 100.
Lo haremos con las diferentes opciones
* while
* for (usando “range”) y sin usar un condicional, solo con el uso del rango
"""

# while
print("======================while (impares) ======================")
i = 1

"""
Para obtener los impares para mostrarlos, ponemos la condición si la
división de entre 2 es diferente a 0 en el resto. Con eso sabemos que 
es impar y lo mostramos
"""
while i <= 100:
    if ( i % 2 != 0): print(i)
    i += 1

# for
print("======================for (impares) ======================")
"""
En este caso aplicamos que por iteración haga + 2. Empezando de 1, que es
impar, si vamos sumando + tendremos 1, 3, 5, 7, 9, 11, 13, 15, 17, 
19, 21,...
"""
for value in range(1, 101, 2):
    print(value)
