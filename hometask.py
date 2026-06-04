import sqlite3


conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    password TEXT
)
""")




def authenticate(login, password):


    cursor.execute(
        "SELECT * FROM users WHERE login = ?",
        (login,)
    )

    user = cursor.fetchone()


    if user:
        print("Пользователь уже существует!")


    else:
        cursor.execute(
            "INSERT INTO users (login, password) VALUES (?, ?)",
            (login, password)
        )

        conn.commit()

        print("Пользователь успешно зарегистрирован!")

login = input("Введите логин: ")
password = input("Введите пароль: ")

authenticate(login, password)

conn.close()