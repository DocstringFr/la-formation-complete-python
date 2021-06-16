import logging

LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

if __name__ == "__main__":
    liste = Liste("taches")   
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.afficher()