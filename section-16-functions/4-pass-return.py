# Sentencia "pass"

def function_one(): pass

def function_two():
    pass

# Sentencia -return (un valor)

def add(a = None, b = None):
    if a != None and b != None:
        return a + b
    try:
        raise ValueError("Debemos de especificar los dos valores")
    except ValueError as value_error_message:
        print(value_error_message)

x = add(1, 2)   # 3
x = add(1)      # None
x = add(1, 56)  # 57
x = add(1, 34)  # 35
x = add(-10)    # None