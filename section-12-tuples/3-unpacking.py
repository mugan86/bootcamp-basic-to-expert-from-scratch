# Mismo número de variables que elementos

tuple_elements = ("java", "python", "kotlin")

(java_value, python_value, kotlin_value) = tuple_elements
"""
java_value = "java"
python_value = "python"
kotlin_value = "kotlin"
"""

# Diferentes número de variables sobre los elementos de la tupla

(java_value, *other_values) = tuple_elements
"""
java_value = "java"
other_values = ["python", "kotlin"]
"""

(*first_values, kotlin_value) = tuple_elements
"""
first_values = ["java", "python"]
kotlin_value = "kotlin"
"""
tuple_elements = ("java", "python", "c#", "kotlin")

(java, *middle_elements, kotlin) = tuple_elements

"""
java = "java"
middle_elements = ["python", "c#"]
kotlin = "kotlin"
"""
print("FINAL")
