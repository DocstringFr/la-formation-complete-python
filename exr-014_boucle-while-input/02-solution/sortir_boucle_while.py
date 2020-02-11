# Solution 1
continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")

# Solution 2
continuer = "o"
while continuer == "o":
    print("On continue !")
    resultat = input("Voulez-vous continuer ? o/n ")
    if resultat != "o":
        break

# Solution 3 avec Python 3.8 uniquement
while (continuer := "o") == "o":
    print("On continue !")
    if (resultat := input("Voulez-vous continuer ? o/n ")) != "o":
        break