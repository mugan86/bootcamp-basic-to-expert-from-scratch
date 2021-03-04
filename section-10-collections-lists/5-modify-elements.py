# string
programming_languages = ["rust", "java", "c#", "python", "typescript"]

# Index +
programming_languages[3] = "c++" # python => c++
programming_languages[4] = "ruby" # typescript => ruby
programming_languages[len(programming_languages) - 1] = "javascript"
# ruby => javascript

# Index -
programming_languages[-3] = "go" # c# => "go"
programming_languages[-2] = "kotlin" # c++ => kotlin
programming_languages[-5] = "scala" # rust => scala
programming_languages[len(programming_languages) * (-1)] = "c++"
# scala => c++
print("*******")

# Selección múltiple

programming_languages = ["rust", "python", "c#", "java", "typescript"]

# Indices +

programming_languages[1: 3] = ["c++"]
# ["rust", "c++", "java", "typescript"]

programming_languages[2: 3] = ["kotlin", "scala", "python"]
# ["rust", "c++", "kotlin", "scala", "python", "typescript"]

# Omitir la posición inicial
programming_languages[: 5] = ["c#", "kotlin"]
# ["c#", "kotlin", "typescript"]

programming_languages[: 1] = ["rust", "c++", "kotlin", "scala", "python"]
# ["rust", "c++", "kotlin", "scala", "python", "kotlin", "typescript"]

# Omitir la posición final
programming_languages[0: ] = ["java"]
# ["java"]
programming_languages[0: ] = ["java", "kotlin", "rust", "scala"]
# ["java", "kotlin", "rust", "scala"]

# Indices -
programming_languages = ["rust", "python", "c#", "java", "typescript"]

programming_languages[-4: -2] = ["scala", "kotlin"]
# ["rust", "scala", "kotlin", "java", "typescript"]


# Omitir la posición inicial
programming_languages[: -1] = ["c++", "c#"]
# ["c++", "c#", "typescript"]


# Omitir la posición final
programming_languages[-5: ] = ["rust", "python", "c#", "java", "typescript"]
# ["rust", "python", "c#", "java", "typescript"]

print("*******")