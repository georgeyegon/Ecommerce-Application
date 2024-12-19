import sqlite3
CONN = sqlite3.connect('ecomm.db')
CURSOR = CONN.cursor()

class Database:
    def create_tables(self):
        sql1 = """
        CREATE TABLE IF NOT EXISTS users
        (
        id INTEGER PRIMARY KEY,
        name varchar(40),
        email varchar(40),
        phone INTEGER
        )"""
        CURSOR.execute(sql1)

        sql2 = """CREATE TABLE IF NOT EXISTS products
        (
        id INTEGER PRIMARY KEY, 
        category varchar(40),
        name varchar(40),
        price INTEGER,
        quantity INTEGER
        )"""
        CURSOR.execute(sql2)

        sql3 = """CREATE TABLE IF NOT EXISTS orders
        (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER,
        product_id INTEGER,
        user_id INTEGER,

        FOREIGN KEY(product_id) REFERENCES products(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
        )"""
        CURSOR.execute(sql3)

        sql4 = """CREATE TABLE IF NOT EXISTS reviews
        (
        id INTEGER PRIMARY KEY,
        review TEXT,
        product_id INTEGER,
        user_id INTEGER,

        FOREIGN KEY(product_id) REFERENCES products(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
        )"""
        CURSOR.execute(sql4)

        CONN.commit()

    def drop_tables(self):
        sql = """DROP TABLE IF EXISTS users"""
        CURSOR.execute(sql)

        sql = """DROP TABLE IF EXISTS products"""
        CURSOR.execute(sql)

        sql = """DROP TABLE IF EXISTS orders"""
        CURSOR.execute(sql)

        sql = """DROP TABLE IF EXISTS reviews"""
        CURSOR.execute(sql)
 
        CONN.commit()

db = Database()

db.drop_tables()
print( "Dropped Tables" )

print( "Creating Tables" )

db.create_tables()
print( "Tables Created" )
