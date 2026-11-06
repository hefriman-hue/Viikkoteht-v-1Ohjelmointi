oppilaat = int(input ("Opiskelijoiden lukumäärä: "))
summa = 0
for i in range (oppilaat):
    arvosana = int(input ("Anna opiskelijan arvosana: "))
    summa = summa + arvosana
keskiarvo = summa / oppilaat
print ("Keskiarvo:", keskiarvo)
if keskiarvo <1:
    print ("Huono tulos")
elif keskiarvo <2:
    print ("Heikko tulos")
elif keskiarvo <3:
    print ("Tyydyttävä tulos")
elif keskiarvo <4:
    print ("Hyvä tulos")
elif keskiarvo <5:
    print ("Kiitettävä tulos")
while True:
    oppilaat = int(input ("Opiskelijoiden lukumäärä:"))
    if oppilaat > 0:
        break
    print(" Oppilaita pitää olla vähäintään yksi.")
summa = 0
for i in range (oppilaat):
    while True:
        arvosana = int(input ("Anna opiskelijoidan arvosana: "))
        if 0 <= arvosana <= 5:
            break
        print ("Arvosanan pitää olla välillä 0-5.")
    summa = summa + arvosana



