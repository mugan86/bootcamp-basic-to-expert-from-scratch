try:
    print("Ejecutando código")
    list_values = [1]
    print(list_values[0])
except IndexError:
    print("Algo ha ido mal (Index Error): ")
    print("Indice no existe")
except Exception as exception_message:
    print("Algo ha ido mal: ")
    print(exception_message)
else: 
    print("Else => Todo ha ido bien")
finally:
    print("Finally ejecutando con errores y sin errores")