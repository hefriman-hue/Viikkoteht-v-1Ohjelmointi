
restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": ["lunch", "dinner"],
        "price_level": 5,
        "location": "Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": ["breakfast", "lunch"],
        "price_level": 3,
        "location": "Tornio"
    },
    {
        "name": "Snacksy Oy",
        "rating": 3.2,
        "reservations": False,
        "services": ["lunch", "dinner", "night"],
        "price_level": 2,
        "location": "Oulu"
    },
    {
        "name": "Pizza Palace",
        "rating": 4.7,
        "reservations": True,
        "services": ["lunch", "dinner"],
        "price_level": 3,
        "location": "Kemi"
    },
    {
        "name": "Morning Cafe",
        "rating": 4.1,
        "reservations": False,
        "services": ["breakfast", "lunch"],
        "price_level": 2,
        "location": "Oulu"
    },
    {
        "name": "Night Bites",
        "rating": 3.9,
        "reservations": True,
        "services": ["dinner", "night"],
        "price_level": 4,
        "location": "Rovaniemi"
    }
]

print("Tervetuloa ravintolahakuun!")

# Kysytään käyttäjän hakuehdot
min_rating = float(input("Monenko tähden ravintolan haluat vähintään? (1-5): "))

max_price = int(input("Minkä hintatason ravintolan haluat maksimissaan? (1-5): "))

reservation = input("Haluatko tehdä etukäteen varauksen? (k/e): ").lower()

if reservation == "k":
    reservation = True
else:
    reservation = False

time = int(input("Mihin kellonaikaan haluat ruokailla? (0-23): "))

# Muutetaan kellonaika palvelutyypiksi
if 6 <= time <= 10:
    service = "breakfast"
elif 11 <= time <= 16:
    service = "lunch"
elif 17 <= time <= 23:
    service = "dinner"
else:
    service = "night"

# Etsitään hakuehtoja vastaavat ravintolat
found_restaurants = []

for restaurant in restaurants:
    if (
        restaurant["rating"] >= min_rating
        and restaurant["price_level"] <= max_price
        and restaurant["reservations"] == reservation
        and service in restaurant["services"]
    ):
        found_restaurants.append(restaurant["name"])

# Tulostetaan hakutulokset
print("\nHakua vastaavat ravintolat:")

if len(found_restaurants) > 0:
    for name in found_restaurants:
        print(name)
else:
    print("Valitettavasti sopivaa ravintolaa ei löytynyt!")
