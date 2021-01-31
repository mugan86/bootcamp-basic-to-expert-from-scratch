# Operadores lógicos AND / OR

a = 1 != 2 or (1 > 0 and 45 <= 90)                 # True
a = (1 != 2 and 1 < 0) or 45 > 90                  # False
a = 1 != 2 or ((1 > 0 and 45 <= 90) and 45 != 78)  # True
a = (1 != 2 and 1 > 0) or 45 > 90 or 45 != 78      # True
a = (2 != 2 and 1 == 0) or 45 > 90                 # False
a = ((56 != 23 and 1 > 0) and 45 > 90)             # False
a = 23 > 2 or (1 > 0 and 45 > 90) or 45 > 78       # True

print("Final")