shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]
#Tulostetaan kuitti
print ("Kuitti ostoksita")
#Lasketaan kokonaishinta
yhteensa=0
for tuote in shopcart:
    print("-", tuote["name"])
    yhteensa+=tuote["price"]
print ()
print("Yhteensä", round(yhteensa,1),"€.")
print ("Tervetuloa uudelleen!")

