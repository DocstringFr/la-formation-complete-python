nombre = input("Entrez un nombre: ")
print(type(nombre))  # retourne <class 'str'>. La fonction input retourne toujours une chaîne de caractères.

# Vous pouvez par la suite convertir la variable nombre en nombre entier grâce à la fonction int
nombre = int(nombre)
print(type(nombre))  # retourne <class 'int'>. La variable a bien été convertie.