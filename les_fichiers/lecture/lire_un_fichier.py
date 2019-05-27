import json

chemin = "/Users/thibh/fichier.json"

with open(chemin, "r") as f:
    liste = json.load(f)
    print(type(liste))
    # json.dump(list(range(10)), f, indent=4)
