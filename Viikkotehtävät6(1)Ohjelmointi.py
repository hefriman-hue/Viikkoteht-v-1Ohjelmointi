suurin = 0
for i in range (5):
    while True:
        try:
            luku = int(input ("Anna numero:" ))
            if luku > 0:
                break
            print ("Luvun pitää olla positiivinen!")
        except ValueError:
            print("Anna kokonaisluku!")
    if luku > suurin:
        suurin = luku
print ("Suurin luku on:", suurin)
