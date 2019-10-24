employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
employes.index("Alex")  # 4
employes.count("Max")  # 2
employes.sort()  # Trie la liste en la modifiant directement : ["Alex", "Carlos", "Martine", "Max", "Max", "Patrick"]
sorted(employes)  # Trie la liste mais ne modifie pas la liste d'origine !
liste_trie = sorted(employes)  # On retourne la liste triée dans une nouvelle liste.

nombres = [10, 1, 5, 15]
nombres.reverse()  # Inverse l'ordre de la liste : [15, 5, 1, 10]
print(nombres)