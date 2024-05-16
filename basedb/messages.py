from database.mysql_connection import DBOperation


class MessagesDB(DBOperation):
    def get_last_message(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Wrap client_sub_domain in a tuple to match the expected parameter format
        db_cursor.execute("select * from messages order by created_at desc limit 1")
        res = db_cursor.fetchone()[2]
        db.close()
        if res:
            return res
        else:
            return None

    def get_last_message_msg(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Wrap client_sub_domain in a tuple to match the expected parameter format
        db_cursor.execute("select * from messages order by created_at desc limit 1")
        res = db_cursor.fetchone()[3]
        db.close()
        if res:
            return res
        else:
            return None

