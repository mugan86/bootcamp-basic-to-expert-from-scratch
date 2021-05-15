

input_value = input("Introduce la palabra a convertir en acrónimo: ")
values_split = input_value.split()

result = ""
for word in values_split:
    result += word[0].upper()

print(f"Palabra introducida: {input_value} => {result}")