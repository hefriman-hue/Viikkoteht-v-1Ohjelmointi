teksti=input("Anna jokin teksti:")
if teksti=="":
    print("Antamasi teksti on tyhjä.")
else:
    kaannetty=teksti [::-1]
    print(kaannetty)
    if teksti==kaannetty:
        print("Palindromi: KYLLÄ")
    else:
        print("Palindromi:ei")
