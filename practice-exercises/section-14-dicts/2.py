# Sin constructor
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
print(type(the_blacklist))
print(the_blacklist)

# Con constructor
the_blacklist = dict(
    name = "The Blacklist",
    first_air_date = "2013-06-01",
    seasons = 8,
    duration = "40-55",
    genres = ["Drama", "Crimen", "Misterio"],
    tags =  [
        "terrorist",
        "fbi",
        "investigation",
        "criminal mastermind",
        "crime lord",
        "hidden identity",
        "criminal consultant"
    ]
)
print(type(the_blacklist))
print(the_blacklist)

