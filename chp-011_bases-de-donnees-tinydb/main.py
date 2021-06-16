from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)


users = db.table("Users")
roles = db.table("Roles")

users.insert({"name": "Patrick", "salary": 25000})
users.insert({"name": "Paul", "salary": 35000})
users.insert({"name": "Julie", "salary": 45000})

roles.insert_multiple([
    {"name": "Pythonista"},
    {"name": "Javaista"},
    {"name": "JavaScripta"},
])