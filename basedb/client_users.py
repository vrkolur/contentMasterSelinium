from database.mysql_connection import DBOperation


class ClientUserDB(DBOperation):
    def get_last_client_user(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        # Wrap client_sub_domain in a tuple to match the expected parameter format
        db_cursor.execute("select * from client_users order by created_at desc limit 1")
        res = db_cursor.fetchone()[1]
        db.close()
        if res:
            return res
        else:
            return None

    def get_client_user_by_sub_domain(self, client_sub_domain):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM clients where sub_domain={client_sub_domain}")
        res = db_cursor.fetchone()
        db.close()
        return res
