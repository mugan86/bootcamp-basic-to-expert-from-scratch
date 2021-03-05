# Referenciando la información de las listas
original_list = ["rust", "java", "c#", "python", "typescript"]

list2 = original_list

list2[0] = "c++"

# Trabajamos con la clonación del contenido de la lista

original_list = ["rust", "java", "c#", "python", "typescript"]

copy_list = original_list.copy()

original_list[0] = "kotlin"
copy_list[1] = "javascript"
copy_list.append("scala")

original_list.clear()
print("*****")