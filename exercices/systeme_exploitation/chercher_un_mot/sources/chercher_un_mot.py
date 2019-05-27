import glob

dossier = "/Users/thibh/formation-developpeur-python/exercices/systeme_exploitation/chercher_un_mot/sources/dossier_exemple/**"
files = glob.glob(dossier, recursive=True)
