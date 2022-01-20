"""
\'	Comilla simple: Añade la comilla simple si usamos strings con comillas simples	
\n	Nueva línea: Hace un salto de línea
\t	Tabulación: Añade una tabulación posterior
\b	Backspace: Retroceso		
\\	Contra barra: Se asegura que añada la contrabarra	
"""

# 1.- Comillas simples

a = 'Hola, soy \'Anartz Mugika Ledo\'' # Hola, soy 'Anartz Mugika Ledo'
print("1- " + a)
# 2.- Salto de línea \n

a = 'A: Hola\nB: Hola, ¿Qué tal?\nA: Bien, ¿ Y tu? '
print("2- " + a)
'''A: Hola
B: Hola, ¿Qué tal?
A: Bien, ¿ Y tu? '''

# 3.- Tabulación

a = 'A: Hola\tB: Hola, ¿Qué tal?\tA: Bien, ¿ Y tu? '
print("3- " + a)
# 'A: Hola    B: Hola, ¿Qué tal?    A: Bien, ¿ Y tu? '

# 4.- Retroceso \b

a = 'Hola\br' # Hol
print("4- " + a)
a = 'Hola\b\bdd' # Ho
print("4- " + a)
a = 'Hola\b\b\bddd' # H
print("4- " + a)

# 5.- Contra barra \\

n_value = 'C:\\nuevo' # C:\nuevo
print("5(n)- " + n_value)
"""
n_value = 'C:\nuevo' 
Resultado:
C:
uevo
"""

t_value = 'C:\\tablas' # C:\tablas
print("5(t)- " + t_value)
"""
t_value = 'C:\tablas' 
Resultado:
C:  ablas
"""