from functools import reduce

# reduce(funcion, iterable)

# Resta

def substraction(total, value):
    return total - value

numbers = [2, 4, 5, 10] # -17

x = reduce(substraction, numbers)
print(x)

x_lambda = reduce(lambda total, value: total - value, numbers)
print(x_lambda)

# Suma de restos de division 2

def rest_two(total, value):
    return total + value % 2
# [2, 4, 5, 10]
x = reduce(rest_two, numbers) # 3
print(x)

x_lambda = reduce(lambda total, value: total + value % 2, numbers) # 3
print(x_lambda)