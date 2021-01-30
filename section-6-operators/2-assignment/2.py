# Módulo / Exponencial / División + redondeo al entero má cercano

# Igualdad (asignación)
x = 2
y = 10
z = 4

# Módulo
x %= 2 # x = x % 2 = 2 % 2 = 0 (1 en la división)
y %= 3 # y = y % 3 => 10 % 3 = 1 ( 3 en la división)
z %= 3 # z = z % 3 => 4 % 3 = 1 (1 en la división)

# Exponencial
x, y , z  = 2, 1, 4

x **= 3  # x = x ** 3 => 2 * 2 * 2 = x = 8
y **= 23 # y = y ** 23 => 1 * 1 ... * 1 = y = 1
z **= 2  # z = z ** 2 => 4 * 4 = z = 16

x, y , z  = 10, 23, 45

# División
x //= 3  # x = x // 3 => int(10 / 3) = x = 3
y //= 7  # y = y // 3 => int(23 / 7) = y = 3
z //= 7  # z = z // 7 => int(45 / 7) = z = 6

print("Final")