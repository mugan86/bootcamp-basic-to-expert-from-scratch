# Vamos a trabajar con el condicional "if" únicamente

languages = input('Lenguajes de programación (Espacios para separar)\n')
# Kotlin Java C#
convert_list = True

if(convert_list):
    languages = languages.split() # ['Kotlin', 'Java', 'C#']

print(languages)