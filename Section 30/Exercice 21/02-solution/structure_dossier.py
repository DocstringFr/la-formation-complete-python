import os

chemin = "/Users/thibh/dossier_test"

d = {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}

for key, value in d.items():
	for dossier in value:
		chemin_dossier = os.path.join(chemin, key, dossier)
		os.makedirs(chemin_dossier, exist_ok=True)