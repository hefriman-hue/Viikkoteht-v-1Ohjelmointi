alaraja=int(input("Anna alueen alaraja:"))
ylaraja=int(input("Anna ylaraja:"))
loydetty = False
for luku in range(alaraja,ylaraja +1):
    if luku % 5 != 0:
        print (f"{luku} ei ole jaollinen viidellä, hylätään.")
        continue
    if luku % 7 != 0:
            print(f"{luku} ei ole jaollinen seitsemällä, hylätään.")
            continue
    print(f"Luku {luku} on jaollinen 5:llä ja 7:llä.")
    print ("Lopetetaan haku.")
    loydetty = True
    break
if not loydetty:
    print("Alueelta ei löytynyt sopivaa arvoa.")



