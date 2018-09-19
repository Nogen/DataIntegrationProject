

class Dao:

    CRTTBL = "CREATE TABLE IF NOT EXISTS %s(%s)"
    INSERTING = "INSERT INTO %s VALUES(%s)"
    SELECTING = "SELECT * FROM %s %s"

    def __init__(self, dbobj, tablename="table"):
        self.cursor = dbobj.getConnection()
        self.name = dbobj.getName()
        self.tablename = tablename
        self.table = self.name + self.tablename

    def getTablename(self):
        return self.tablename

    def createTable(self, columns, scheme):
        str = ""
        for k in columns:
            str += k + " " + scheme[k] + ","
        self.cursor.execute(Dao.CRTTBL % (self.tablename, str[:-1]))

    def insertRow(self, data):
        self.cursor.execute(Dao.INSERTING % (self.tablename, data))

    def dataViewer(self, limit = ''):
        limit = "LIMIT %s" % limit if (limit) else limit
        print limit
        return self.cursor.execute(Dao.SELECTING % (self.tablename, limit))
