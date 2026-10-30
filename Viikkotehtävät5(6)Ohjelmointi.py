elokuva = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Rikos, Draama",
    "duration": 154
}
print("Silmukalla:")
for tieto in elokuva.values():
    print(tieto)

print()
print("Ilman silmukkaa:")
print(elokuva["name"])
print(elokuva["year"])
print(elokuva["director"])
print(elokuva["genre"])
print(elokuva["duration"])
