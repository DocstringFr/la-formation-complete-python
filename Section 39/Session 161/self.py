class Voiture:
    def __init__(self, marque):
        self.marque = marque

    def afficher_marque(self):
        print(f"La voiture est une {self.marque}")

voiture_01 = Voiture("Lamborghini")
voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_01)
