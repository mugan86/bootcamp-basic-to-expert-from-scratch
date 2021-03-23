# Manejo excepciones básico

try:
    14 / 0
except:
    print("No podemos dividir con cero")

try:
    print(x)
except Exception as exception_message:
    print(exception_message)


print("Final")