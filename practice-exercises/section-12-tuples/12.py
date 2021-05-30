"""
Ordena una tupla con bucles.
Ejemplo:
tuple_list = (1,45, 23, 44, 55, 2, 230, 4555)
Resultado esperado: 
(1, 2, 23, 44, 45, 55, 230, 4555)
"""

tuple_list = (1,45, 23, 44, 55, 2, 230, 4555)
list = []
for i in tuple_list:
    if len(list) == 0:
        list.append(i)
    elif len(list) > 0:
        position = 0
        while True:
            if (list[position] > i):
                list.insert(position, i)
                break
            else: 
                if (len(list) - 1 == position):
                    list.append(i)
                    break
                else:
                    position += 1
                
print(tuple(list))
            
    
    