from util import strFilter

class CsvDataConverter:

    TIME = " 23:12:18"
    MAP = {"INT" : (lambda x: strFilter(x).sanitizeDouble()  or "NULL"),
            "DOUBLE" : (lambda x: strFilter(x).sanitizeDouble()  or "NULL") ,
             "DATE" : (lambda x: x + CsvDataConverter.TIME),
             "VARCHAR(256)" : (lambda x:  "\"" +  strFilter(x, "\"").sanitize() + "\"")
    }


    def __init__(self, row, elmtypes):
        self.row = row
        self.elmtype = elmtypes

    def values2Query(self):
        str = ""
        for i in range(len(self.row)):
            str += CsvDataConverter.MAP[self.elmtype[i]](self.row[i]) + ","
        return str[:-1]
