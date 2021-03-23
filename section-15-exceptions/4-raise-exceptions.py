try:
    print("Ejecutando código")
    pos_index_select = 5
    list_values = [1, 12, 13, 14, 16, 'anartz']  # 0 - 5
    if len(list_values) - 1 < pos_index_select:
        raise IndexError(f"El índice seleccionado es {pos_index_select}" +
                        f" y la longitud de la lista es de {len(list_values)} valores.")
except IndexError as index_error_message:
    print("Algo ha ido mal (Index Error): ")
    print(index_error_message)
except Exception as exception_message:
    print("Algo ha ido mal: ")
    print(exception_message)
else:
    print("Else => Todo ha ido bien")
finally:
    print("Finally ejecutando con errores y sin errores")
