import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(
    prenom text,
    nom text
)
""")

d = {"prenom": "Paul", "nom": "Dupond"}
c.execute("INSERT INTO employees VALUES (:prenom, :nom)", d)

conn.commit()
conn.close()