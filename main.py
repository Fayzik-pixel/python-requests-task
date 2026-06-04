data = response.json()
users = data["users"]

print(len(users))   # сколько пользователей
print(users[0])     # первый пользователь

for user in users:
    print(user["id"], user["firstName"], user["lastName"])




import sqlite3

# Подключаемся к базе
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создаём таблицу если её нет
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        email TEXT,
        phone TEXT
    )
""")

# Вставляем каждого пользователя
for user in users:
    cursor.execute("""
        INSERT OR IGNORE INTO users (id, first_name, last_name, age, email, phone)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user["id"], user["firstName"], user["lastName"], user["age"], user["email"], user["phone"]))

conn.commit()
conn.close()

print("Готово! Пользователи вставлены в БД")