import sqlite3


class DbCreator:

    def __init__(self, dbname):
        self.name = dbname
        self.db = sqlite3.connect(dbname)
        self.connection = self.db.cursor()

    def getConnection(self):
        return self.connection

    def close(self):
        self.db.commit()
        self.db.close()

    def getName(self):
        return self.name

    def __enter__(self):
        return self.connection

    def __exit__(self, type, value, traceback):
        self.close()
