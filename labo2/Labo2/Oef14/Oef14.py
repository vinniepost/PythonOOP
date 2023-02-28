
print("Wat is je boodschap?");
yetToBeIncrypted = input();
shift = int(input("Hoeveel letter wil je het verschuiven? \n"))

shifted_text = "";
for char in yetToBeIncrypted:
    if char.isalpha():
        ascii_val = ord(char);
        shifted = (ascii_val - 65 + shift) % 26 + 65;
        shifted_car = chr(shifted);
        shifted_text += shifted_car
    else:
        shifted_text += char


print(shifted_text);