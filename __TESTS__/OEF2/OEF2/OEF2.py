from tokenize import Double


class Nummers:
    def __init__(self, Getal1, Getal2):
        self.Getal1 = Getal1
        self.Getal2 = Getal2
        pass

    def Som(self):
        som = self.Getal1 + self.Getal2
        return som
    def Verschil(self):
        verschil = self.Getal2-self.Getal1
        return verschil
    def Quotient(self):
        if self.Getal2 == 0:
            print("Kan niet delen door 0")
            exit
        quotient = self.Getal1/self.Getal2
        return quotient
    def Product(self):
        product = self.Getal1*self.Getal2
        return product

test = Nummers(10,3)
print(test.Quotient())