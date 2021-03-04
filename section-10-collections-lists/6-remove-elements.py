list_remove = ["java", "python", "c++", "c#", "java"]

# remove

list_remove.remove("java")
# ["python", "c++", "c#", "java"]
list_remove.remove("java")
# ["python", "c++", "c#"]
list_remove.remove("c++")
# ["python", "c#"]

# pop
list_pop = ["java", "python", "c++", "c#", "java"]

list_pop.pop()
# ["java", "python", "c++", "c#"]
list_pop.pop(1)
# ["java", "c++", "c#"]
list_pop.pop(0)
# ["c++", "c#"]

# del
list_del = ["java", "python", "c++", "c#", "java"]

del list_del[1]
# ["java", "c++", "c#", "java"]
del list_del[0]
# ["c++", "c#", "java"]
del list_del[1]
# ["c++", "java"]

list_clear = ["java", "python", "c++", "c#", "java"]

list_clear.clear()
# []
elements_count = len(list_clear)

print("********")