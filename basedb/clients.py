from database.mysql_connection import DBOperation


class ClientsDB(DBOperation):
    def get_client_by_id(self, client_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM clients WHERE id={client_id};")
        res = db_cursor.fetchone()
        db.close()
        if res:
            return res[2]
        else:
            return None

    def get_client_by_sub_domain(self, client_sub_domain):
        try:
            db = self.connect_to_db()
            db_cursor = db.cursor()
            # Use parameterized query to prevent SQL injection
            db_cursor.execute("SELECT * FROM clients WHERE sub_domain = %s", (client_sub_domain,))
            res = db_cursor.fetchall()
            db.close()
            if res:
                # Assuming you want to return the third column, adjust as needed
                return res[2]
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_client_status(self,client_sub_domain):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM clients where sub_domain={client_sub_domain}")
        res = db_cursor.fetchone()
        db.close()
        if res:
            return res[3]
        else:
            return None
