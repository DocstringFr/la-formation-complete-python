import random

nombre_mystere = random.randint(0, 10)
nombre_utilisateur = input("Quel est le nombre mystère ? ")

resultat = int(nombre_utilisateur) == nombre_mystere

print(resultat)
