# Operadores lógicos AND / OR / NOT

a = not(1 != 2 or (1 > 0 and 45 <= 90) )                    # False
a = not((1 != 2 and 1 < 0) or 45 > 90 )                     # True
a = not(1 != 2) or not((1 > 0 and 45 <= 90) and 45 != 78)   # False
a = (1 != 2) or not((1 > 0 and 45 <= 90) and 45 != 78)      # True
a = (1 != 2 and 1 > 0) or not(45 > 90) or 45 != 78          # True

print("Final")