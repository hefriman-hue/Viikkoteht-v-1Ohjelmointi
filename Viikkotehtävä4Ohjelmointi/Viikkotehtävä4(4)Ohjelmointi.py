luku=int(input("Anna luku:"))
good_division = False
if luku % 3 == 0:
    good_division = True
if luku % 5 == 0:
    good_division = False
if good_division:
    print("Liku on sopiva.")
else:
    print("Luku ei ole sopiva.")

