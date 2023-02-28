print("Wat is de maand (schrijf voluit)");
maand = input();
print("Geef de dag als int");
dag = int(input());

if (maand == "maart"&dag>=20)|maand == "april"|maand == "mei"|(maand == "juni"&dag<21):
    print("Het is lente");
elif (maand == "juni"& dag>= 21)| maand == "juli"|maand == "augustus"|(maand == "september"&dag<22):
    print("Het is zomer");
elif (maand == "september"&dag>=22)| maand == "oktober"|maand == "november"|(maand == "december"&dag<21):
    print("Het is herst");
elif (maand == "december"&dag>=21)|maand == "januari"|maand == "februari"| (maand == "maart"&dag<20):
    print("Het is winter");
else:
    print("Invalid input");