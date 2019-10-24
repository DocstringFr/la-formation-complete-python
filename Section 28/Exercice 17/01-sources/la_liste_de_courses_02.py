import os
import json

dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")
 
if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []
 
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""