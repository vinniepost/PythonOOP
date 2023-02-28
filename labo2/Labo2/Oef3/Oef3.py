print("Geef me een letter");
letter = input();

match letter:
    case ("a" | "e" | "i" | "o" | "u"):
        print(f"U gaf de klinker {letter}");
    case ("y"):
        print(f"{letter} wordt soms als klinker gebruikt en soms niet");
    case _:
        print(f"De letter {letter} is geen klinker");
