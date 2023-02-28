aantalKleineFlessen = int(input("Hoeveel kleine flesjes heb je? "))
aantalGroteFlessen = int(input("Hoeveel grote flesjes heb je? "))

waardeKleineFless = 0.12
waardeGroteFless = 0.25

totaleWaarde = (waardeKleineFless * aantalKleineFlessen) + \
    (waardeGroteFless * aantalGroteFlessen)
print(f"Je krijgt {totaleWaarde} terug")
