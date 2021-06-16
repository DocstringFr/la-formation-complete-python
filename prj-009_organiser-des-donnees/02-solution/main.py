with open("/Users/thibh/Documents/prenoms.txt", "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open("/Users/thibh/Documents/prenoms_final.txt", "w") as f:
    f.write("\n".join(sorted(prenoms_final)))