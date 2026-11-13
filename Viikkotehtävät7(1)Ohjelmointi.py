cafe = {
    "name": "Imaginary Cafe Oy",
    "website": "https://edu.frostbit.fi/sites/cafe",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
 "location": {
    "city": "Rovaniemi",
    "address": "Testikuja 22",
    "zip_code": "96200"
    }
}
print(cafe ["name"])
print(cafe["location"]["address"])
print(cafe["location"]["zip_code"],cafe["location"]["city"])
print()
print(cafe["website"])
print("Palvelut:", ", ".join(cafe["categories"]))
