import sqlite3

class Product:
    DB_NAME = "products.db"

    @staticmethod
    def connect():
        return sqlite3.connect(Product.DB_NAME)

    @staticmethod
    def create_table():
        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        create table if not exists products (
            id integer primary key autoincrement,
            name text not null,
            price real not null,
            quantity integer not null,)
            
            
        
        
        """)
        conn.commit()
        conn.close()

    def __init__(self, name, price, quantity, product_id=None):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def save(self):
        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        insert into products (name, price, quantity) 
        values (?, ?, ?)
        """,(self.name, self.price, self.quantity))

        conn.commit()
        conn.close()

        print("Product saved")


    @staticmethod
    def get_all_users():
        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        select * from products""")
        products = cursor.fetchall()

        conn.close()
        return products

    @staticmethod
    def get_object(product_id):
        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        select * from products where id = ?""",(product_id,))
        product = cursor.fetchone()

        conn.close()
        return product

    @staticmethod
    def delete(product_id):
        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        delete from products where id = ?""",(product_id,))

        conn.commit()
        conn.close()

        print("Product deleted")

    @staticmethod
    def update(product_id, new_name, new_price, new_quantity):

        conn = Product.connect()
        cursor = conn.cursor()

        cursor.execute("""
        update products
        set name = ?, price = ?, quantity = ?
        where id = ?""",(new_name, new_price, new_quantity, product_id))

        conn.commit()
        conn.close()

        print("Product updated")



Product.create_table()
p1 = Product("IPhone 15", 1200, 5)
p1.save()
p2 = Product("Samsung S24", 1000, 8)
p2.save()
print(Product.get_all_users())
print(Product.get_object(1))
Product.update(1, "IPhone 15 Pro", 1500, 3)
Product.delete(2)
print(Product.get_all_users())


