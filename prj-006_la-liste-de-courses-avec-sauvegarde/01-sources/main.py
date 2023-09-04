"""
Le but de cet exercice est de repartir de notre script de la liste de course et d'ajouter un système de sauvegarde sur le disque.


👉 Quelques astuces pour mener à bien ce projet (ne pas lire si tu souhaites essayer tout seul !)
Pour cet exercice tu vas devoir utiliser le module os et le module json.

Pour récupérer le chemin complet vers le script Python, tu peux utiliser la variable __file__ qui est définie par Python et qui contient le chemin complet vers le script exécuté.

Avec le module os, tu peux ensuite récupérer le dossier parent et concaténer le nom du fichier json (liste.json) à ce dossier, avec la fonction os.path.join.

Pour lire et écrire dans un fichier json, on utilise respectivement les fonctions load et dump du module json.

Il faudra également t'assurer que le fichier existe avant de lire son contenu. Pour ça tu peux utiliser la fonction os.path.exists du module os.
"""


import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]



while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)
