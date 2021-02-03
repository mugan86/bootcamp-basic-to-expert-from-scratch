# Valores booleanos

# Miramos el resultado desde otros tipos de datos

# Números
a = bool(0)                     # False
a = bool(-12383829)             # True
a = bool(0)                     # False
a = bool(12354245322)           # False
# Strings
a = bool("")                # False
a = bool(" ")               # True
a = bool("")                # False
a = bool("Anartz")          # True
a = bool("-----")           # True
# Uso de Operadores Relacionales y Lógicos

# Relacionales ==, !=, >, < , >=, <=
a = 45 == 34    # False
a = 45 != 34    # True
a = 45 > 34     # True
a = 45 < 34     # False
a = 45 >= 34    # True
a = 45 <= 34    # False
# Lógicos and, or, not
a = 45 == 34 and 36 == 36               # False
a = 45 == 34 or 36 == 36                # True
a = 45 != 34 and 36 == 36 or 34 > 8     # True
a = not(45 == 34 and 36 == 36)          # True

print("Final")