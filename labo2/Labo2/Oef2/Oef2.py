print("Geef de leeftijd van een mens om te weten hoe oud de persoon is in hondenjaren.");
userInput = int(input());


if (userInput <= 21):
    leeftijd = userInput / 10.5;
    leeftijd = round(leeftijd, 2);
    print(f"De leeftijd in hondenjaren is {leeftijd}");
else:
    beginJaren = 21
    leeftijd = userInput - beginJaren;
    leeftijd = round(((leeftijd/4) + (beginJaren/10.5)),2)
    print(f"De leeftijd in hondenjaren is {leeftijd}")
