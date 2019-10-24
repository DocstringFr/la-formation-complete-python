class Voiture:
    marque = "Lamborghini"

voiture_01 = Voiture()
voiture_02 = Voiture()

# print(voiture_01.marque)
# print(voiture_02.marque)

Voiture.marque = "Porsche"

# print(voiture_01.marque)
# print(voiture_02.marque)

voiture_01.marque = "Peugeolt"
voiture_02.marque = "Volkswagen"

print(Voiture.marque)
print(voiture_01.marque)
print(voiture_02.marque)