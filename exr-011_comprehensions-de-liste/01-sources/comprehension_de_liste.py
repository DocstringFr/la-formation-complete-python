nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i in nombres if i % 2 == 0 ]
print(nombres_pairs)

# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [i in nombres if i>= 0]
print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [i*2 in nombres]

print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [i else -i for i in nombres if i % 2 == 0 ]

print(nombres_inverses)
