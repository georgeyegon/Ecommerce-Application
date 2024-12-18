from lib.config import CONN, CURSOR

class Products:
    # Create product
    @classmethod
    def create_product(cls, category, name, price, quantity):
        sql = "INSERT INTO products( category, name, price, quantity) VALUES( ?, ?, ?, ?)"
        CURSOR.execute(sql, ( category, name, price, quantity))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def fetch_all_products(cls):
        sql = "SELECT * FROM products"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    


    @classmethod
    def search_product_by_id(cls, product_id):
        sql = "SELECT * FROM products WHERE id = ?"
        CURSOR.execute(sql, (product_id,))
        return CURSOR.fetchone()

    @classmethod
    def search_product_by_name(cls, name):
        sql = "SELECT * FROM products WHERE name = ?"
        CURSOR.execute(sql, (name,))
        return CURSOR.fetchall()
    
    @classmethod
    def search_product_by_category(cls, category):
        sql = "SELECT * FROM products WHERE category = ?"
        CURSOR.execute(sql, (category,))
        return CURSOR.fetchall()

    @classmethod
    def update_product_by_id(cls, product_id, category, name, price, quantity):
        sql = "UPDATE products SET category = ?, name = ?, price = ?, quantity = ? WHERE id = ?"
        CURSOR.execute(sql, ( category, name, price, quantity, product_id))
        CONN.commit()
        return product_id


    
