import sqlite3

import os

class Sqlite_DB():

    db_path = None

    def __init__(self, db_path):
        self.db_path = db_path
        if not os.path.isfile(self.db_path):
            print("INFO: creating sqlite database")
            self._create_sqlite_db()
        else:
            print("INFO: sqlite database found")

    def _create_sqlite_db(self):
        query = """CREATE TABLE data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_key text,
            date_time int,
            field text,
            data real)"""
        self.execute(query)

    def execute(self, query, query_dict=None):
        records = []

        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row # Row class: life = easy
            c = conn.cursor()

            results = None
            if query_dict:
                results = c.execute(query, query_dict)
            else:
                results = c.execute(query)

            for row in results:
                records.append(row) # TODO: Find a better way than this
                print(row)

            conn.commit() # Covers queries and admin operations

        except Exception as inst:
            print("CRIT: Caught exception - {}".format(inst))
            # stop eating this exception and re-raise it to the views
        finally:
            conn.close()

        return records
