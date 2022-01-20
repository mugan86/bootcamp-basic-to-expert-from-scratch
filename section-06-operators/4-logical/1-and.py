# Operadores lógicos AND

a = 1 == 1 and 1 > 0                                # True
a = 1 != 2 and 1 > 0 and 45 <= 90                   # True
a = 1 != 2 and 1 > 0 and 45 > 90                    # False
a = 1 != 2 and 1 > 0 and 45 <= 90 and 45 != 78      # True
a = 1 != 2 and 1 > 0 and 45 > 90 and 45 != 78       # False

print("Final")