import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather=json.loads(raw_data)
alueet= {
    "lapland": "Lappi",
    "middle": "Maan keskiosa",
    "south": "Etelä-Suomi"
}
for alue in alueet:
    summa = 0
    maara = 0
    for paikka in weather:
        if paikka ["area"] == alue:
            summa += paikka ["wind"]
            maara += 1
        if maara > 0 :
            keskiarvo = round(summa/maara,1)
            print ("Keskimääräinen tuuli,",alueet[alue] +":",keskiarvo, "m/s")