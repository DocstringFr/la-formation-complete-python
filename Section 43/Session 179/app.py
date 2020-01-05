import json

fichier = "settings.json"

with open(fichier, "r") as f:
    settings = json.load(f)

settings["fontSize"] = 15

with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)
