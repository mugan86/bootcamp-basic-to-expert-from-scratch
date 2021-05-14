"""
Escribe un programa que haga una suma de todos los números que tenemos 
dentro de una lista.

Solo se permitirán los números que sean de tipo float / int.

Si alguno de ellos no lo es, lo ignoramos sin hacer ninguna suma.

"""

case_one = [1, 2, 3, 4, 5, 6, 7]
case_two = [1, "Anartz", 4]
case_three = [1, "Anartz", True, 90]

total = 0
for value in case_three:
    if ( type(value) == int or type(value) == float): total += value

print(f"Total: {total} from {case_three}")
