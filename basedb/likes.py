from database.mysql_connection import DBOperation


class LikesDB(DBOperation):
    def get_last_like_status(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("select * from likes order by created_at desc limit 1")
        res = db_cursor.fetchone()[1]
        db.close()
        return res

    def get_last_like_user_id(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("select * from likes order by created_at desc limit 1")
        res = db_cursor.fetchone()[2]
        db.close()
        if res:
            return res
        else:
            return None
