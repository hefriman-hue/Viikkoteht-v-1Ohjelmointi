while True:
    luku = int(input ("Minkä luvun kertotaulun haluat nähdä? (1-10), 0 lopettaa ohjelman:"))
    if luku == 0:
        break
    if luku< 1 or luku >10:
        print ("vääränlainen luku.")
        continue
    for i in range (1,11):
        print (luku,"x", i, " =", luku * i)
