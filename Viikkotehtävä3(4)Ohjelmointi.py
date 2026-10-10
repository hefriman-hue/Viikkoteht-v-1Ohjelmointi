pisteet =int(input(" Anna pistemäärä"))
if pisteet < 0 or pisteet > 100:
    print ("Pistemäärä ei ole mahdollinen.")
if pisteet < 0 or pisteet > 100:
    print("Pistemäärä ei ole mahdollinen.")
elif pisteet <= 50:
    print("Arvosana: 0")
elif pisteet <= 60:
    print("Arvosana: 1")
elif pisteet <= 70:
    print("Arvosana: 2")
elif pisteet <= 80:
    print("Arvosana: 3")
elif pisteet <= 90:
    print("Arvosana: 4")
else:
    print("Arvosana: 5")
