PI = 3.14159265359
straal = int(input("wat is de straal "))
hoogte = int(input("Wat is de hoogte "))
basis = (straal * straal * PI)

volume = round((basis * hoogte),2)

print(volume)