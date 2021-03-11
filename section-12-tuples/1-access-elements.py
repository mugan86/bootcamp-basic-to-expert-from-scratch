# Inicializar las tuplas para la selección
languages = tuple(("java", "rust", "c#", "python", "typescript"))

check_type = type(languages) # <class 'tuple'>

# Añadimos + tuplas de diferentes valores
numbers_list = (12, 13.4, 12 + 45j)
check_type = type(numbers_list) # <class 'tuple'>
bool_list = (True, True, False, False)
check_type = type(bool_list) # <class 'tuple'>
mixed_elements = ("anartz", 12, True, (12, 12), 12 + 45j)
check_type = type(mixed_elements) # <class 'tuple'>

# Seleccionar de manera única
select = languages[0]                               # java
select = languages[1]                               # rust
select = languages[len(languages) - 1]              # typescript

# Indices negativos
select = languages[len(languages) * (-1)]           # java
select = languages[len(languages) * (-1) + 1]       # rust
select = languages[-1]                              # typescript
languages = tuple(("java", "rust", "c#", "python", "typescript"))

# Selección multiple
select = languages[1:4]                     # ("rust", "c#", "python")
select = languages[ : 2]                    # ("java", "rust")
select = languages[2 : ]                    # ("c#", "python", "typescript")

# Indices negativos
select = languages[len(languages) * (-1) + 1:-1] # ("rust", "c#", "python")
select = languages[ : len(languages) * (-1) + 2] # ("java", "rust")
select = languages[len(languages) * (-1) + 2 : ] # ("c#", "python", "typescript")
print("*****")