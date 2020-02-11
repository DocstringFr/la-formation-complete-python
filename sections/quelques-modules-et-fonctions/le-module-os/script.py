import os

chemin = "/Users/thibh/formation-developpeur-python"
dossier = os.path.join(chemin, "dossier", "test")
if os.path.exists(dossier):
    os.removedirs(dossier)