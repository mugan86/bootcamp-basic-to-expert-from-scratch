# Mismo número de variables que elementos

tuple_elements = ("java", "python", "kotlin")

(java_value, python_value, kotlin_value) = tuple_elements

# Diferentes número de variables sobre los elementos de la tupla

(java_value, *other_values) = tuple_elements

(*first_values, kotlin_value) = tuple_elements

tuple_elements = ("java", "python", "c#", "kotlin")

(java, *middle_elements, kotlin) = tuple_elements
print("FINAL")
