import json
import urllib.request
#Haetaan säätiedot internetistä
url= "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather= json.loads(raw_data)
#Etsitään suurin ja pienin tuulennopeus
eniten =max (weather, key=lambda x : x ["wind"])
vahiten = min (weather, key=lambda x : x ["wind"])
print ("Tänään eniten tuulee sijainnissa:",
       eniten["location"],eniten["wind"]," m/s",)
print ("Tänään vähiten tuulee sijainnissa:",
       vahiten["location"],vahiten["wind"], " m/s")



