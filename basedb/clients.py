from database.mysql_connection import DBOperation


class ClientsDB(DBOperation):


    def get_client_by_sub_domain(self, client_sub_domain):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT * FROM clients WHERE sub_domain = %s", (client_sub_domain,))
        res = db_cursor.fetchone()[2]
        db.close()
        if res:
            return res
        else:
            return None

    def get_client_status(self, client_sub_domain):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT * FROM clients WHERE sub_domain = %s", (client_sub_domain,))
        res = db_cursor.fetchone()[3]
        db.close()
        return res
