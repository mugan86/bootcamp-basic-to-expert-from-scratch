"""
Realizar un programa que imprima en pantalla los números impares del 100 al 1 (incluidos).
Lo haremos con las diferentes opciones
* while
* for (usando “range”) y sin usar un condicional, solo con el uso del rango
"""

# while
print("======================while (impares) ======================")
i = 100

"""
Para obtener los impares para mostrarlos, ponemos la condición si la
división de entre 2 es diferente a 0 en el resto. Con eso sabemos que 
es impar y lo mostramos
"""
while i >= 1:
    if ( i % 2 != 0): print(i)
    i -= 1

# for
print("======================for (impares) ======================")
"""
En este caso aplicamos que por iteración haga + 2. Empezando de 99, que es
impar, si vamos restando - tendremos 99, 97, 95, 93, 91...
"""
for value in range(99, -1, -2):
    print(value)
