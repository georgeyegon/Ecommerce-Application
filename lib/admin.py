from lib.config import CONN, CURSOR

class Admin:

    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password
    
    @classmethod
    def create_product(cls, category, name, price, quantity):
        sql = "INSERT INTO products( category, name, price, quantity) VALUES( ?, ?, ?, ?)"
        CURSOR.execute(sql, ( category, name, price, quantity))
        CONN.commit()
        return CURSOR.lastrowid