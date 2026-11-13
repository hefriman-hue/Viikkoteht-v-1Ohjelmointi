import json
import urllib.request
from collections import Counter
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.urlopen(url)
raw_data = urllib.request.urlopen(req).read().decode ("UTF-8")
warnings = json.loads(raw_data)
#Lasketaan varoitukset kaupungeittain
kaupungit = []
for varoitus in warnings :
    kaupungit.append(varoitus ["city"])
maarat =Counter(kaupungit)
kaupunki, maara = maarat.most_common(1) [0]
print ("Eniten liukastumisvaroituksia:")
print (kaupunki, maara, "varoitusta")
#Järjestetään varoitukset aikaleiman mukaan
jarjestetyt = sorted (
    warnings,
    key =lambda x: x ["timestamp"],
    reverse = True
    )
print ( " \n5 viimeisintä liukastumisvaroitusta:")
for varoitus in jarjestetyt [:5]:
    print (varoitus ["city"], varoitus["timestamp"])
