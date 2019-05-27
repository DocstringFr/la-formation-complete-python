chemin = "/Users/thibh/fichier.txt"
f = open(chemin, "r")
print(f.read())
f.seek(0)
contenu = f.read()
print(contenu)
f.close()