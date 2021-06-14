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

str1 = 'Bienvenido'
print (str1[:6] + ' Anartz')

str1 = "BootcampPython!!"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

my_name = "anartz mugika"

print("anartz" == my_name)
print("anartz" is my_name)
print("bienvenido al fantástico mundo del desarrollo en python".title())

txt = "Hola, mi nombre es Anartz"

print(txt.swapcase())

print(txt)
    
    