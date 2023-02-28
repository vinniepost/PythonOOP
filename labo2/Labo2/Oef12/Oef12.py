som = 0;
i = 0
while(True):
    print("Geef een getal of geen 0 om de loop te beiendigen")
    userInput = int(input());
    if userInput == 0:
        break
    som += userInput
    i +=1;

Gemiddelde = som/i
print(f"Het gemiddelde van alle getallen die je gaf is {Gemiddelde}")