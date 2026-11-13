#Luodaan lista elokuvista
movies =[
    {"name": " Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Titanic", "year": 1997},
    {"name": "Avatar", "year": 2009},
    {"name": "Frozen", "year": 2013}
]
#Luodaan kaksi tyhjää listaa
new_movies=[]
old_movies=[]
#Käydään elokuvat läpi
for movie in movies:
    if movie["year"] >=2000:
        new_movies.append(movie["name"])
    else:
        old_movies.append(movie["name"])
#Tulostetaan uudet elokuvat
print ("Seuraavat elokuvat on julkaistu 2000-luvulla:")
for movie in new_movies:
    print (movie)
print()
#Tulostetaan vanhat elokuvat
print ("Seuraavat elokuvat on julkaistu ennen vuotta 2000:")
for movie in old_movies:
    print (movie)

