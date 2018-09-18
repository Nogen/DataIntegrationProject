from util import strFilter

class CsvDataConverter:

    TIME = " 23:12:18"
    MAP = {"INT" : (lambda x: strFilter(x).sanitizeDouble()  or "NULL"),
            "DOUBLE" : (lambda x: strFilter(x).sanitizeDouble()  or "NULL") ,
             "DATE" : (lambda x: x + CsvDataConverter.TIME),
             "VARCHAR(256)" : (lambda x:  "\"" +  strFilter(x, "\"").sanitize() + "\"")
    }


    def __init__(self, row, elmtypes):
        """
            Args:
                row (string array): elementi di una riga del Csv
                elmtypes (string array): tipo degli elemnti della riga del csv
        """
        self.row = map(lambda x: str(x), row)
        self.elmtype = map(lambda x: str(x), elmtypes)

    def values2Query(self):
        """
            Returns:
                una stringa degli elementi puliti pronti per una query
        """
        str = ""
        for i in range(len(self.row)):
            str += CsvDataConverter.MAP[self.elmtype[i]](self.row[i]) + ","
        return str[:-1]
