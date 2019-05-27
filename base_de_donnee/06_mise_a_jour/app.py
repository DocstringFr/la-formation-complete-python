import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(
    prenom text,
    nom text,
    salaire int
)
""")

d = {"salaire": 20000, "prenom": "Patrick", "nom": "Dupont"}

c.execute("""UPDATE employees SET salaire=:salaire
WHERE prenom=:prenom AND nom=:nom""", d)

conn.commit()
conn.close()