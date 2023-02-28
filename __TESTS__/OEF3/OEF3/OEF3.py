from enum import Enum

class Klass(Enum):
    K1 = 1
    K2 = 2
    K3 = 3

class Student:
    def __init__(self, Naam: str, Leeftijd: int, Klas: Klass, PuntenCommunicatie: int, PuntenProgrammingPrinciples: int, PuntenWebTech: int):
        self.Naam = Naam
        self.Leeftijd = Leeftijd
        self.Klas = Klas
        self.PuntenCommunicatie = PuntenCommunicatie
        self.PuntenProgrammingPrinciples = PuntenProgrammingPrinciples
        self.PuntenWebTech = PuntenWebTech
        self.Test = 15

    def BerekenTotaalCijfer(self):
         Gemiddelde = (self.PuntenCommunicatie + self.PuntenProgrammingPrinciples + self.PuntenWebTech)/3
         return Gemiddelde

    def ToonOverzicht(self):
        print(f"{self.Naam}, {self.Leeftijd}")
        print(f"Klas: {self.Klas}")
        print("")
        print("**********")
        print(f"Communicatie:   {self.PuntenCommunicatie}")
        print(f"Programming Principles: {self.PuntenProgrammingPrinciples}")
        print(f"Web Tech: {self.PuntenWebTech}")
        print(f"Gemiddelde: {Student.BerekenTotaalCijfer(self)}")





test = Student("Vinnie Post",21, Klass.K1, 12,10,20)
test.ToonOverzicht()
