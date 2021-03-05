

numbers_list = [12, -23, -34, 35, 45, 100, 12839]
str_list = ["tomb raider", "assasins creed", "crash bandicoot"]

# orden ascendente

numbers_list.sort()
# [-34, -23, 12, 35, 45, 100, 12839]

str_list.sort()
# ["assasins creed", "crash bandicoot", "tomb raider"]

# Orden descendente

numbers_list.sort(reverse=True)
# [12839, 100, 45, 35, 12, -23, -34]

str_list.sort(reverse=True)
# ["tomb raider", "crash bandicoot", "assasins creed"]

# Diferenciar entre mayúsculas / minúsculas
str_list.append("Mario")
str_list.append("Little Big Planet")
str_list[0] = "Tomb Raider"

# Orden ascendente
str_list.sort()

# Orden descendente
str_list.append("sonic")
str_list.sort(reverse=True)
print("*******")