from lib.config import CONN, CURSOR

class Orders:

    cart = []

    @classmethod
    def add_to_cart(cls, name, price, quantity ):
        sql = "INSERT INTO orders( name, price, quantity) VALUES( ?, ?, ?)"
        item = (name, price, quantity)
        cls.cart.append(item)
        CURSOR.execute(sql, ( name, price, quantity))
        CONN.commit()
        return CURSOR.lastrowid
 
    @classmethod
    def delete_by_order_id(cls, order_id):
        sql = "DELETE FROM orders WHERE id = ?"
        CURSOR.execute(sql, (order_id,))
        CONN.commit()
        return order_id
    
    @classmethod
    def fetch_all_orders(cls):
        sql = "SELECT * FROM orders"
        CURSOR.execute(sql)
        return CURSOR.fetchall()


