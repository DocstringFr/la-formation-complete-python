nombre_mystere = 7
nombre = input("Quel est le nombre mystère ? ")

nombre = int(nombre)
if nombre > nombre_mystere:
    print(f"Le nombre mystère est plus petit que {nombre}")
elif nombre < nombre_mystere:
    print(f"Le nombre mystère est plus grand que {nombre}")
else:
    print("Bravo, vous avez trouvé le nombre mystère !")
