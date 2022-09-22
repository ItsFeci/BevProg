#!/usr/bin/env python
# coding: utf8
def string_modositas(input_text):
    letters = {}
    for i in input_text:
        if i in letters: 
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1
    
    print(f"Betuk gyakorisaga:  {str(letters)}")
    ## Betuk forditva kiirasa:
    reverse_text = input_text[::-1]
    print(f"Forditva:  {reverse_text}")
    ## Szavak tomben
    split_words = input_text.split(' ')
    print(f"Listaba rendeyve szavankent:  {split_words}\n")

def cm_to_inch(number, unit):
    if unit == "cm":
            print(f"{number}cm = {number/2.54}inch")
    elif unit == "inch":
        print(f"{number}inch = {number*2.54}cm")
    else:
        print("Not Correct Unit!")


if __name__ == "__main__":

    user_text = input("Adjon meg egy mondatot:\n")
    string_modositas(user_text)
    

    bekert_szam = int(input("Adjon meg egy szamot es egy mertekegyseget (cm/inch):\nSzam: "))
    bekert_mertekegyseg = input("mertekegyseg: ")
    cm_to_inch(bekert_szam,bekert_mertekegyseg)
