import mysql.connector


class DBOperation:
    def __init__(self):
        pass

    def connect_to_db(self):
        content_master_dev = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#1Varun0104",
            database='content_master_dev'
        )

        return content_master_dev
