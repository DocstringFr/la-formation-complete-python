import random

nombre_mystere = random.randint(0, 50)
nombre_essais = 5
essais = 0

while essais < nombre_essais:
    nombre = input("Quel est le nombre mystère ? ")

    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        continue

    nombre = int(nombre)

    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()
    
    essais += 1

print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}")
    