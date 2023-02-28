class RapportModule(object):
    def __init__(self, punt):
        self.punt = punt
    
    def Print(self):
        if self.punt < 50:
            print("Niet geslaagd!")
        elif self.punt <= 68:
            print("Voldoende")
        elif self.punt <= 75:
            print("Onderscheiding")
        elif self.punt <= 85:
            print("Grote onderschijding")
        else:
            print("Grootste onderscheiding")

test = RapportModule(88)
test.Print()
