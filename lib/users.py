from lib.config import CONN, CURSOR

class Users:
    @classmethod
    def create_user(cls, name, email, phone):
        sql = "INSERT INTO users(name, email, phone) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (name, email, phone))
        CONN.commit()
        return CURSOR.lastrowid

    @classmethod
    def get_user(cls, user_id):
        sql = "SELECT * FROM users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchone()
    
    @classmethod
    def fetch_all_users(cls):
        sql = "SELECT * FROM users"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def update_user_by_id(cls, user_id, name, email, phone):
        sql = "UPDATE users SET name = ?, email = ?, phone = ? WHERE id = ?"
        CURSOR.execute(sql, (name, email, phone, user_id))
        CONN.commit()
        return user_id

    @classmethod
    def delete_user_by_id(cls, user_id):
        sql = "DELETE FROM users WHERE id = ?"
        CURSOR.execute(sql, (user_id,))
        CONN.commit()
        return user_id

    @classmethod
    def fetch_all_products(cls):
        sql = "SELECT * FROM products"
        CURSOR.execute(sql)
        return CURSOR.fetchall()


