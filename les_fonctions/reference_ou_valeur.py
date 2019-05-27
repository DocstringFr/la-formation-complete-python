# a = 5

# def change_a():
#     a = 10
#     print(id(a))

# change_a()
# print(id(a))











# nombres = [10, 20, 30]

# def ajoute_40():
#     print(id(nombres))
#     nombres.append(40)

# ajoute_40()
# print(id(nombres))

nombres = [10, 20, 30]

def ajoute_40(liste):
    liste.append(40)

ajoute_40(nombres)
print(nombres)


