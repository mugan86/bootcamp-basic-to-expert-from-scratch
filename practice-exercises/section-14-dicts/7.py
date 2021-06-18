the_blacklist = {
    "name": "The Blacklist",
    "first_air_date": "2013-06-01",
    "seasons": 8,
    "duration": "40-55",
    "genres": ["Drama", "Crimen", "Misterio"],
    "tags": [
        "terrorist",
        "fbi",
        "investigation",
        "criminal mastermind",
        "crime lord",
        "hidden identity",
        "criminal consultant"
    ]
}
print(f"Diccionario inicial: {the_blacklist}")

# Eliminar buscando por clave
the_blacklist.pop('tags')
the_blacklist.pop('genres')
the_blacklist.pop('seasons')

print(f"Diccionario Final: {the_blacklist}")
