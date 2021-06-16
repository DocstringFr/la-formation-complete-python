# On déclare deux variables
a = b = ""

# Tant que a et b ne sont pas des nombres, on boucle
while not (a.isdigit() and b.isdigit()):
    
    # On demande deux nombres à l'utilisateur
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

# On affiche le résultat de l'addition
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")