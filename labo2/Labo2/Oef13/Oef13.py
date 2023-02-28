eindfactuur = 0;
aantalOnder3 = 0;
aantal3Tot12 = 0;
aantal12Tot65 = 0;
aantalBoven65 = 0;
i = 1;


while True:
    print(f"Wat is de leeftijd van persoon {i}")
    userish = input()
    if userish == "":
        break
    userInput = int(userish);
    if userInput < 3:
        eindfactuur += 0;
        aantalOnder3 +=1;
    elif userInput < 12:
        eindfactuur += 15;
        aantal3Tot12 += 1;
    elif eindfactuur > 65:
        eindfactuur += 20;
        aantalBoven65 += 1;
    else:
        eindfactuur += 30;
        aantal12Tot65 += 1;
    i += 1;
eindfactuur = "{:.2f}".format(eindfactuur)
print(f"De verdeling van tikkets zijn als volgt: \n Onder 3 jaar: {aantalOnder3} \n Tussen 3 en 12: {aantal3Tot12} \n Tussen 12 en 65: {aantal12Tot65} \n Boven 65: {aantalBoven65} \n \n De Totaalprijs zal {eindfactuur} zijn ")