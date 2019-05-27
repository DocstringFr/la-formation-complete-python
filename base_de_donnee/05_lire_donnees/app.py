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


c.execute("SELECT * FROM employees WHERE")
donnees = c.fetchall()
print(donnees)
premier = c.fetchone()
print(premier)


conn.commit()
conn.close()