import random as r

uitkomstRoulettewiel = r.randint(0,37) #tussen 0 en 

match uitkomstRoulettewiel:
    case (1|3|5|7|9|12|14|16|18|19|21|23|25|27|30|32|34|36):
        kleur = "Rood";
    case (2|4|6|8|10|11|13|15|17|20|22|24|26|28|29|31|33|35):
        kleur = "Zwart";
    case (0|37):
        kleur = "Groen";
match (uitkomstRoulettewiel%2):
    case 0:
        Evenheid = "Even";
    case 1:
        Evenheid = "Oneven";
match (uitkomstRoulettewiel>=18& uitkomstRoulettewiel != 0):
    case True:
        GetalOnderAchtien = "Getal onder en 18";
    case False:
        GetalOnderAchtien = "Getal boven 18";

print(f"Het getal was {uitkomstRoulettewiel}. \n Dit wilt zeggen dat {kleur} won \n Dit wilt zeggen dat {Evenheid} won.  \n Dit wilt zeggen dat {GetalOnderAchtien} won")