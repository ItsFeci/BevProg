#!/usr/bin/env python
# coding: utf8
from colorama import Fore
from colorama import Style


def main():
#1.feladat
    ## Szoveg bekerese majd betuk megszamolasa
    letters = {}
    input_text = input(f"1.(feladat)\nAdjon meg egy mondatot:\n{Fore.GREEN}")

    for i in input_text:
        if i in letters: 
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1
    
    print(f"{Fore.RESET}Betuk gyakorisaga:  {str(letters)}")
    ## Betuk forditva kiirasa:
    reverse_text = input_text[::-1]
    print(f"Forditva:  {reverse_text}")
    ## Szavak tomben
    split_words = input_text.split(' ')
    print(f"Listaba rendeyve szavankent:  {split_words}\n")

######################################################################################
#2.feladat
    number = int(input(f"(2.feladat)\nAdjon meg egy szamot es egy mertekegyseget (cm/inch):\nSzam:{Fore.GREEN} "))
    unit = input(f"{Fore.RESET}mertekegyseg:{Fore.GREEN} ")
    

    if unit == "cm":
            print(f"{Fore.RESET}{number}cm = {number/2.54}inch")
    elif unit == "inch":
        print(f"{Fore.RESET}{number}inch = {number*2.54}cm{Fore.RESET}")
    else:
        print(f"{Fore.RESET}Not Correct Unit!")



   

if __name__ == "__main__":
	main()