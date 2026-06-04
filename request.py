import requests
import sqlite3

response = requests.get("https://dummyjson.com/users")
print(response.status_code)
print(response.json())

data = response.json()
users = data["users"]

print(len(users))
print(users[0])

for user in users:
    print(user["id"]), user["firstName"], user["lastName"]


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("Drop table if exists users")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id integer primary key,
    first_name text,
    last_name text,
    age integer,
    email text,
    phone text
    )
""")

for user in users:
    cursor.execute("""
    insert or ignore into users (id, first_name, last_name, age, email, phone)
    values (?, ?, ?, ?, ?, ?)
    """, (user["id"], user["firstName"], user["lastName"], user["age"], user["email"], user["phone"]))

conn.commit()
conn.close()
print("Successfully created users")



conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()