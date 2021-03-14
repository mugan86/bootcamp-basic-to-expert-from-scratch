elements = {'a', 'b', 12, 23, 23 + 35j}
# Borrar con búsqueda => remove() / discard()
elements.remove('a')
# elements.remove('a') <==== Salta excepción KeyError
elements.discard('a')
elements.discard(12)
elements.discard(23)
# Eliminar el último elemento => pop()
elements = {1, 2, 3, 4, 5, 6, 7, 8}
delete_item = elements.pop()
delete_item = elements.pop()
delete_item = elements.pop()
# Eliminar todo el contnido sin destruir el conjunto => clear()
elements.clear()
# 0 elementos en el conjunto
elements.add("anartz")
elements.update({1, 2, 3, 3})
# Eliminar todo el contenido destruyendo el conjunto => del

del elements
elements = {'a'}
elements.add("ddddd")

print("FINAL")