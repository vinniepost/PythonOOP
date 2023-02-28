print("Welk jaar zou je willen controleren of het een schrikkeljaar is");
MogenlijkSchrikkeljaar = int(input());

if MogenlijkSchrikkeljaar%400 == 0:
    print("Dit is een schrikkeljaar")
elif MogenlijkSchrikkeljaar%100==0:
    print("Dit is geen schrikkeljaar")
elif MogenlijkSchrikkeljaar%4==0:
    print("Dit is een schrikkeljaar")
else:
    print("Dit is geen schrikkeljaar")
