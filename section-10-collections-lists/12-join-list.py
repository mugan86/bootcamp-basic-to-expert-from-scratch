# Operador +

list1 = ["java", "python", "c++"]
list2 = ["kotlin", "javascript"]

list3 = list1 + list2
# ["java", "python", "c++", "kotlin", "javascript"]

list3 = list2 + list1
# ["kotlin", "javascript", "java", "python", "c++" ]


# Bucle for con append
list1 = ["java", "python", "c++"]
list2 = ["kotlin", "javascript"]

# Añadir elementos de la lista 1 en la 2
for item in list1:
    list2.append(item)
# list2 = ["kotlin", "javascript", "java", "python", "c++" ]

list2 = ["kotlin", "javascript"]
# Añadir elementos de la lista 2 en la 1
for item in list2:
    list1.append(item)
# list1 = ["java", "python", "c++", "kotlin", "javascript" ]

# extend()

list1 = ["java", "python", "c++"]
list2 = ["kotlin", "javascript"]

list1.extend(list2)
# ["java", "python", "c++", "kotlin", "javascript"]

# Reiniciar lista 1 con valores por defecto
list1 = ["java", "python", "c++"]
list2.extend(list1)
# ["kotlin", "javascript", "java", "python", "c++" ]

print("++++")