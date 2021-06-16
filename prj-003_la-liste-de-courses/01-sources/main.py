"""
Dans ce projet, tu vas devoir créer un programme en ligne de commande qui permet de manipuler une liste de courses.

👉 Déroulé du script
Le programme doit permettre de réaliser 5 actions :
- Ajouter un élément à la liste de courses
- Retirer un élément de la liste de courses
- Afficher les éléments de la liste de courses
- Vider la liste de courses
- Quitter le programme

Tu dois donc demander à l'utilisateur de choisir parmi une de ces action en entrant un nombre de 1 à 5.

Tu dois gérer le cas de figure où l'utilisateur ne rentre pas un nombre compris entre 1 et 5 ou s'il rentre par exemple des lettres ou un autre symbole invalide. Dans ce cas, tu dois afficher de nouveau le menu avec les options disponibles, jusqu'à ce que l'utilisateur choisisse une option valide.

Dans ce projet, tu ne dois pas sauvegarder la liste dans un fichier ou une base de donnée.

Le but ici est juste d'interagir avec l'utilisateur et de manipuler une liste en fonction de son choix.

Bonne chance pour cet exercice ?

Prends le temps de bien décrire toutes les étapes en français avant de te lancer dans le code !


Quelques éléments pour t'aider :

Pour boucler sur un itérable et récupérer en même temps l'indice de l'itération, tu peux utiliser la fonction enumerate :

>>> for i, element in enumerate("Python"):
>>>     print(i, element)
0 "P"
1 "y"
2 "t"
3 "h"
4 "o"
5 "n"
Pour sortir d'un script en ligne de commande, tu peux utiliser le module sys et la fonction exit :

import sys
sys.exit()
Cela aura pour effet de mettre fin au script en cours d'exécution.
"""