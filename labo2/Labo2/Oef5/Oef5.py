print("Geef een maand waarvan je de lengte wenst te weten");
opgevraagdeMaand = input();
match opgevraagdeMaand:
    case ("januari" | "maart"| "mei" | "juli" | "augustus"| "oktober"|"december"):
        print("Deze maand heeft 31 dagen")
    case ("april"|"juni"|"september"|"november"):
        print("Deze maande heeft 30 dagen")
    case ("februari"):
        print("Deze maand kan 28 of 29 dagen hebben")
    case _: 
        print("De input is fout")
