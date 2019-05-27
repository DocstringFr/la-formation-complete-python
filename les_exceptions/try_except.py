a = 5

try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par zero impossible.")
except TypeError:
    print("La variable b n'est pas du bon type.")
except NameError as e:
    print("Erreur:", e)
finally:
    print("Fin du bloc.")