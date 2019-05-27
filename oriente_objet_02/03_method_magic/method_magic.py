class Voiture:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse

    def __str__(self):
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}."

porsche = Voiture("Porsche", 200)
affichage = str(porsche)
print(affichage)