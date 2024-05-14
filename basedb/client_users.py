from database.mysql_connection import DBOperation


class ClientUserDB(DBOperation):
    def get_client_user_by_id(self, client_user_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM client_users WHERE id={client_user_id};")
        res = db_cursor.fetchone()
        db.close()
        return res

    def get_client_user_by_sub_domain(self, client_sub_domain):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM clients where sub_domain={client_sub_domain}")
        res = db_cursor.fetchone()
        db.close()
        return res
