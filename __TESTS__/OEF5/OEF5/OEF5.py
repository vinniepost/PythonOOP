
class Rechthoek:
    def __init__(self, lengte, breete):
        if lengte>0:
            self.lengte = lengte
        else: self.lengte = 0
        if breete>0:
            self.breete = breete
        else: self.breete = 0
    def ToonOppervlakte(self):
        self.oppervlakte = self.lengte*self.breete
        return self.oppervlakte

class Driehoek:
    def __init__(self, basis, hoogte):
        if basis>0:
            self.basis = basis
        else: self.basis = 0
        if hoogte>0:
            self.hoogte = hoogte
        else: self.hoogte = 0
    def ToonOppervlakte(self):
        self.oppervlakte = (self.basis*self.hoogte)/2

rechthoek = Rechthoek(10,2)
print(rechthoek.ToonOppervlakte())
