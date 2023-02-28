hoeveelheid = int(input("Hoeveel geld heb je op de bank gezet? "))

begin = 0
eind = 3
rente = 0.012

while begin < eind:
    hoeveelheid += round((hoeveelheid * rente), 2)
    print(f"Aantal jaar {begin}, hoeveelheid geld {hoeveelheid}")
    begin += 1