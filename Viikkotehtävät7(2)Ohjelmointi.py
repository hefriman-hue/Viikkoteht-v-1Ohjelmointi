#Luodaan kolme listaa
fruits = ["apple", "pear", "banana"]
berries= ["strawberry", "bluberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]
#Yhdistetään listat inventory-listaksi
inventory = [fruits, berries, vegetables]
#Tulostetaan kaikki sanat allekkain
for lista in inventory:
    for tuote in lista:
        print(tuote)
