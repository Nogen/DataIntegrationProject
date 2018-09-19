from csvpckge.util import strFilter
from csvpckge.util import DataTypes

class CsvDataConverter:

    TIME = " 23:12:18"
    NULL = "NULL"
    MAP = {DataTypes.Int : (lambda x: strFilter(x).sanitizeDouble()  or CsvDataConverter.NULL),
            DataTypes.Double : (lambda x: strFilter(x).sanitizeDouble()  or CsvDataConverter.NULL) ,
            DataTypes.Date : (lambda x: x + CsvDataConverter.TIME),
             DataTypes.Text : (lambda x:  "\"" +  strFilter(x, "\"").sanitize() + "\"")
    }


    def __init__(self, row, elmtypes):
        """
            Args:
                row (string array): elementi di una riga del Csv
                elmtypes (string array): tipo degli elemnti della riga del csv
        """
        if (not row or not elmtypes):
            raise ValueError("args cannot be null")
        if (len(row) != len(elmtypes)):
            raise ValueError("Args's length should be equal")
        self.row = map(lambda x: str(x), row)
        self.elmtype = map(lambda x: str(x), elmtypes)


    def values2Query(self):
        """
            Returns:
                una stringa degli elementi puliti pronti per una query
        """
        str = ""
        for i in range(len(self.row)):
            if(self.elmtype[i] in CsvDataConverter.MAP):
                str += CsvDataConverter.MAP[self.elmtype[i]](self.row[i]) + ","
        return str[:-1]
