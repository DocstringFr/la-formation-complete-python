utilisateurs = ["Paul", "Pierre", "Marie"]
"Paul" in utilisateurs  # retourne le booléen True

if "Paul" in utilisateurs:
    print("Bonjour Paul, bon retour parmi nous!")

if "Paul" in utilisateurs:
    utilisateurs.remove("Paul")

# Fonction aussi avec des chaînes de caractères
"Java" in "Javascript"  # retourne le booléen True