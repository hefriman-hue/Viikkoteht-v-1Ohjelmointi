def show_personal_info():
    print("Matti Meikäläinen")
    print("Sodankylä")
    print("Ohjelmistosuunnittelija")

def count_seconds(hours, minutes, seconds):
    total = hours * 3600 + minutes * 60 + seconds
    return total

def magazine_serial_check(serial):
    if (len(serial) == 9 and
            serial[4]=="-" and
            serial[:4].isdigit() and
            serial[5:].isdigit()):
        print("Oikea ISSN.")
    else:
        print("Väärä ISSN.")



def show_numbered_list(title, data):
    print()
    print(title)
    for number, name in enumerate(data, start=1):
        print(f"{number}. {name}")


import math
def box_volume (width,height, depth):
    volume = width * height * depth
    return round(volume, 2)
def ball_volume (radius):
    volume = (4 * math.pi * radius **3) / 3
    return round(volume, 2)
def pipe_volume (radius, length):
    volume = math.pi * radius ** 2 * length
    return round(volume, 2)

import random
def generate_lotto(count, excluded=None):
    lotto_numbers = []
    if excluded is None:
        excluded = []
    while len(lotto_numbers) < count:
        number = random.randint(1, 40)
        if number not in lotto_numbers and number not in excluded:
            lotto_numbers.append(number)
    lotto_numbers.sort()
    return lotto_numbers

def convert_money(amount, from_currency, to_currency):
    rates ={
        "€":1,
        "$":1.2,
        "£":0.9,
        "kr": 10.3
    }
    euros =amount / rates[from_currency]
    result =euros * rates[to_currency]
    return round(result, 2)








