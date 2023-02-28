print("Hoeveel zijde heeft je figuur?")
aantalZijde = int(input());

match aantalZijde:
    case 3:
        print("Je figuur is een driehoek")
    case 4:
        print("Je figuur is een vierhoek")
    case 5:
        print("Je figuur is een vijfhoek")
    case 6:
        print("Je figuur is een zeshoek")
    case 7:
        print("Je figuur is een zevenhoek")
    case 8:
        print("Je figuur is een achthoek")
    case 9:
        print("Je figuur is een negenhoek")
    case 10:
        print("Je figuur is een tienhoek")
    case _:
        print("Dit figuur ligt buiten de scope van dit programma")