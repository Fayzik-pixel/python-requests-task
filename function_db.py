import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()

def create_user(name, age):
    cursor.execute(
        " insert into users (name, age) values (?, ?)",
        (name, age)
    )
    conn.commit()
    print("foydalanuvchi qoshildi")

def get_users():
    cursor.execute("select * from users")
    users = cursor.fetchall()

    for user in users:
        print(user)

def get_user_by_id(user_id):
    cursor.execute(
        "select * from users where id = ?",
    (user_id,)
    )
    users = cursor.fetchall()
    print(users)

def update_user(user_id, new_name, new_age):
    cursor.execute(
        """
        update users
        set name = ?, age = ?
        where id = ?
        """,
        (new_name, new_age, user_id)
    )

    conn.commit()
    print("foydalanuvchi yangilandi")

def delete_user(user_id):
    cursor.execute(
        "delete from users where id = ?",
        (user_id,)
    )

    conn.commit()
    print("foydalanuvchi o`chirildi")

create_user("ali", 20)
create_user("john", 25)

