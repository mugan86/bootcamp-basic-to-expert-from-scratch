set1 = {5, 10, 3, 15, 2, 20}
# 6 - No hay duplicados y no descarta ninguno
print(len(set1))
set2 = {5, 5, 5, 5, 5, 5}
# 1 - El 5 está duplicado 6 veces y solo se deja uno de ellos
print(len(set2))
set3 = {5, 10, 5, 5, 5, 5, 5, 5}
# 2 - El 5 está duplicado muchas veces y solo se deja una vez con el 10
print(len(set3))
set4 = {5, 10, 3, 5, 5, 5, 5, 5, 5}
# 3 - El 5 está duplicado, 10 y 3
print(len(set4))
