aantalDagen = int(input("Aantal dagen? "))
aantalUren = int(input("Aantal uren? "))
aantalMinuten = int(input("Aantal Minuten? "))
aantalSeconden = int(input("Aantal Seconden? "))

aantalSeconden += aantalMinuten*60 + aantalUren*60*60 + aantalDagen * 60 * 60 * 24
print(f" {aantalSeconden} seconden")
