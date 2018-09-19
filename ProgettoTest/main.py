from csvpckge import Csv2Obj
from csvpckge import DbCreator
from csvpckge import Dao
from csvpckge import CsvDataConverter
import sqlite3

csvname = "Db_creato.csv"
dbname = "prova.db"
tablename = "DbTot"
csvobj = Csv2Obj(csvname, delimiter=";")
schema = csvobj.getSchema()
columns = csvobj.getColumnNames()
print "csv converted to obj"

db = DbCreator(dbname)
print "db created"
dao = Dao(db, tablename = tablename)
dao.createTable(columns, schema)
print "Table created"
print "inserting data... "

for row in csvobj.getDataIterator():
    query = CsvDataConverter(row, csvobj.getColumnTypes()).values2Query()
    dao.insertRow(query)
print "data inserted"

db.close()
