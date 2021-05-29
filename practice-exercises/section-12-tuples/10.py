"""
10.- Permutar los valores de estas dos tuplas:
tuple_one = (23, 34)
tuple_two = (34, 45)

Final: 
tuple_one = (34, 45)
tuple_two = (23, 34)

"""

tuple_one = (23, 34)
tuple_two = (34, 45)
print("Inicio")
print(tuple_one, tuple_two)
tuple_one, tuple_two = tuple_two, tuple_one
print("Final")
print(tuple_one, tuple_two)
