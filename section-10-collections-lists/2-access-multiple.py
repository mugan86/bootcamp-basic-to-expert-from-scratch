programming_languages = ["rust", "python", "c#", "java", "typescript"]

# Indices +

values = programming_languages[1: 3] 
# "python", "c#"
values = programming_languages[2: len(programming_languages) - 1] 
# "c#", "java"

# Omitir la posición inicial
values = programming_languages[: len(programming_languages) - 1] 
# "rust", "python", "c#", "java"
values = programming_languages[: 3] 
# "rust", "python", "c#"

# Omitir la posición final
values = programming_languages[0: ] 
# "rust", "python", "c#", "java", "typescript"
values = programming_languages[5: ] 
# []

# Indices -
programming_languages = ["rust", "python", "c#", "java", "typescript"]

values = programming_languages[-4: -2] 
# "python", "c#"
values = programming_languages[-3: -1] 
# "c#", "java"

# Omitir la posición inicial
values = programming_languages[: -1] 
# "rust", "python", "c#", "java"
values = programming_languages[: -2] 
# "rust", "python", "c#"

# Omitir la posición final
values = programming_languages[len(programming_languages) * (-1): ] 
# "rust", "python", "c#", "java", "typescript"
values = programming_languages[-90: ] 
# "rust", "python", "c#", "java", "typescript"
print("*******")