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

c.execute("DELETE FROM employees")

conn.commit()
conn.close()