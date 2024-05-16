from database.mysql_connection import DBOperation


class ArticlesDB(DBOperation):


    def get_last_article(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Wrap client_sub_domain in a tuple to match the expected parameter format
        db_cursor.execute("select * from articles order by created_at desc limit 1")
        res = db_cursor.fetchone()[1]
        db.close()
        if res:
            return res
        else:
            return None

    def get_last_article_status(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Wrap client_sub_domain in a tuple to match the expected parameter format
        db_cursor.execute("select * from articles order by created_at desc limit 1")
        res = db_cursor.fetchone()[5]
        db.close()
        return res

    def get_article_by_title(self, title):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Corrected SQL query with parameter binding
        db_cursor.execute("SELECT * FROM articles WHERE title=%s", (title,))
        res = db_cursor.fetchone()
        db.close()
        return res
