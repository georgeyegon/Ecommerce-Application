from lib.config import CONN, CURSOR

class Reviews:
    # create review
    @classmethod
    def create_review(cls, review, product_id, user_id):
        sql = "INSERT INTO reviews(review, product_id, user_id) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (review, product_id, user_id))
        CONN.commit()

        return CURSOR.lastrowid

    @classmethod
    def get_reviews_by_user_id(cls, user_id):
        sql = "SELECT * FROM reviews WHERE user_id = ?"
        CURSOR.execute(sql, (user_id,))
        return CURSOR.fetchall()

    @classmethod
    def get_review_by_product_id(cls, product_id):
        sql = "SELECT * FROM reviews WHERE product_id = ?"
        CURSOR.execute(sql, (product_id,))
        return CURSOR.fetchall()

    @classmethod
    def fetch_all_reviews(cls):
        sql = "SELECT * FROM reviews"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def delete_review_by_id(cls, review_id):
        sql = "DELETE FROM reviews WHERE id = ?"
        CURSOR.execute(sql, (review_id,))
        CONN.commit()
        return review_id


