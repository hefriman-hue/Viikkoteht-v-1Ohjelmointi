import string
import secrets
pituus = int(input("Anna salasanan pituus:"))
pienet = string.ascii_lowercase
isot=string.ascii_uppercase
numerot=string.digits
erikoismerkit = "-_^~?*$#!+%@"
salasana =[
    secrets.choice(pienet),
    secrets.choice(isot),
    secrets.choice(numerot),
    secrets.choice(erikoismerkit),
    ]
kaikki =pienet+isot+numerot+erikoismerkit
for i in range(pituus-4):
    salasana.append(secrets.choice(kaikki))
secrets.SystemRandom().shuffle(salasana)
valmis ="".join(salasana)
print("Salasanaehdotus:", valmis)
