# Descontador

iterations_limit = 10

# Iterador
for value in range(iterations_limit, 0, -1):
    print(value)

# Aplicamos recursión

def discount_values(value):
    if value <= 0: return
    print(value)
    return discount_values(value - 1)

print(discount_values(2))

# Factorial
# n! => n = 3 => 3 * 2 * 1 = 6

n = 6 # 720
result = 1

for value in range(1, n + 1):
    result *= value

print("{}! = {}".format(n, result))

# Recursion
def factorial_number(n):
    return n * factorial_number(n -1) if n > 1 else 1

print(factorial_number(1))  # 1
print(factorial_number(2))  # 2
print(factorial_number(3))  # 6
print(factorial_number(4))  # 24
print(factorial_number(5))  # 120
print(factorial_number(6))  # 720