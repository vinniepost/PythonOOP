
class Pizza:
    def __init__(self, Toppings:str, Diameter:int = 1, Price:float = 1):
        if Toppings != None:
            self.Toppings = Toppings
        if Price>=0:
            self.Price = Price
        if Diameter>=0:
            self.Diameter = Diameter
    def Print(self):
        print(f"De topping is: {self.Toppings}")
        print(f"De Diameter is: {self.Diameter} cm")
        print(f"De prijs is: {self.Price} euro")


pizza = Pizza("Annanas",15,4)
print(pizza.Print())