
from ctypes.wintypes import FLOAT


lengte = int(input("Geef de lengte van de kamer? "))
breete = int(input("Geef de breete van de kamer? "))

oppervlakte = float(lengte * breete)

print(f"Een kamer van lengte {lengte} meter en breete {breete} meter heeft een oppervlakte van {oppervlakte} m^2")
