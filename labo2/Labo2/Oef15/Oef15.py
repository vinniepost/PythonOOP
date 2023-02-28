mogenlijkPallendroom = input("Wat is het woord dat je wilt testen? \n");
lengte = len(mogenlijkPallendroom);
isPallendroom = True;

for i in range(lengte):
    if mogenlijkPallendroom[i] != mogenlijkPallendroom[lengte-1-i]:
        isPallendroom = False;

if isPallendroom:
    print(f"{mogenlijkPallendroom} is een pallendroom")
else:
    print(f"{mogenlijkPallendroom} is geen pallendroom")