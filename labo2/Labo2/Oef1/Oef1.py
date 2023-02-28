print("Voer een nummer in om te kijken of het even of oneven is: ")
inputInt = int(input());

#Methode 1

if inputInt%2 == 0:
    print("Even")
else:
   print("Oneven")

#Methode 2

match(inputInt % 2):
    case (0):
        print("Even")
    case _:
        print("Oneven")