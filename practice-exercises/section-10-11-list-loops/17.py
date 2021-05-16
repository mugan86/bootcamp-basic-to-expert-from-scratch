"""
Especificar mediante teclado, cuantos números vamos a tener en una lista 
que debe de ser mínimo 8, usamos como base una lista como la que tenemos
aquí:
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
Luego generaramos una lista de números de 1 hasta el número límite 
especificado por teclado.
La lista tiene que tener mínimo 8 elementos y en el resultado vamos a 
obtener los primeros 4 elementos y los últimos dos elementos.
Ejemplo con 12 elementos:
[1,2,3,4,5,6,7,8,9,10,11,12]
Primeros: 4 elementos: [1,2,3,4]
Últimos: 2 elementos: [1,2,3,4]
"""

start_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# Pedimos el número de caracteres que será para el filtro en el resultado

while True:
    input_value = int(input("Introduce nº elementos: "))
    if (input_value < 8):
        print(f"Debes de especificar 8 ó más. {input_value} no es correcto.")
        continue
    break

# Seleccionamos la cantidad de números y almacenamos en una nueva lista
list_select = start_list[:input_value]

print(f"Lista seleccionada: {list_select}")

#Selección por rangos, hasta el quinto elemento
print(f"Primeros 4 elementos: {list_select[:4]}")

# Hacemos la selección por rango empezando desde 
# la derecha y cogiendo el penúltimo
print(f"Últimos 2 elementos: {list_select[-2:]}")
