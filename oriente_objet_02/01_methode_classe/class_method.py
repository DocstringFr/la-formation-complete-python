class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
