"""
Crear una tupla con nombres de lenguajes de programación, con constructor y sin constructor. 
Comprobamos el tipo con type.
Ejemplos que podremos hacer:
Tupla con un elemento => (“python”)
Tupla con + de un elemento => (“python”, “c#”)

"""
# Sin contructor
print("==============Sin constructor==============")
tuple_one_item = "python" ,
print(tuple_one_item, type(tuple_one_item))
#Create a tuple of one item
tuple_more_items = "python", "c#", "java"
print(tuple_more_items, type(tuple_more_items))
print("==============Con constructor==============")
tuple_one_item = tuple(("python", ))
print(tuple_one_item, type(tuple_one_item))
#Create a tuple of one item
tuple_more_items = tuple(("python", "c#", "java"))
print(tuple_more_items, type(tuple_more_items))