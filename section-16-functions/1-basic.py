# Crear dos funciones

# Sin argumentos
def first_function():
    print("Llamamos a la función básica")


# Argumentos
def add_vat(price):
    type_value = type(price)
    try:
        # Comprobar si es un número
        if (type_value != float and type_value != int):
            # excepción type error
            raise TypeError(f"{price} no es un importe válido")
        print(f"Precio con IVA (16%): { price + price * 0.16}")
    except TypeError as type_error_message:
        print("Type error:")
        print(type_error_message)
    except Exception as exception_message:
        print("General exception:")
        print(exception_message)


first_function()
add_vat(1200)
add_vat("anartz")
add_vat(1900)
