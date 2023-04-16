#conecting to the local database
import sqlite3


class dbcon:
    def __init__(self):
        self.db = "fleet_management.db"
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        