import re
from csvpckge.util import strFilter


class Csv2Obj:

    binding = { "0^[-]?[0-9]+$" : "INT",
            "1^[-]?[0-9]+([,]|[.])[0-9]+$" : "DOUBLE",
            "3^([0-9]{4}|[0-9]{2})[-/][0-9]{2}[-/]([0-9]{2}|[0-9]{4})$" : "DATE",
            "2.+" : "VARCHAR(256)" }

    def __init__(self, csvname, delimiter=","):
        self.csvname = csvname
        self.delimiter = delimiter
        #lista dei tipi delle colonne
        self.elmtypes = []
        #dizionario contenente il mapping tra nome colonna tipo colonna
        self.dictsh = {}
        with open(self.csvname, "rb") as csv:
            #lettura struttura e nomi colonne
            self.header = strFilter(csv.readline(), "\r", "\n").sanitize().split(delimiter)
            #lettura tuple
            self.data = map(lambda str: strFilter(str, "\r", "\n").sanitize(), csv.readlines())

    #restituisce numero di tuple
    def getDataSize(self):
        return len(self.data)

    #restituisce un array con i nomi delle colonne
    def getColumnNames(self):
        return self.header

    #restituisce il dizionario del mapping nome colonna tipo colonna
    def getSchema(self):
        self.dictsh = {}
        row = self.getRow(0)
        for i in range(len(row)):
            for k in sorted(Csv2Obj.binding.keys()):
                res = re.findall(k[1:], row[i])
                if len(res) > 0:
                    self.dictsh[self.header[i]] = Csv2Obj.binding[k]
                    break
        return self.dictsh

    #restituisce un array con il tipo delle colonne
    def getColumnTypes(self):
        self.dictsh = self.dictsh or self.getSchema()
        self.elmtypes = []
        for i in self.header:
            self.elmtypes.append(self.dictsh[i])
        return self.elmtypes

    #restituisce un array delle tuple
    def getData(self):
        return self.data

    #restitusce un oggetto iterabile rappresentante le tuple
    def getDataIterator(self):
        for i in self.data:
            yield i.split(self.delimiter)

    #restituisce la tupla ennesima
    def getRow(self, row_n):
        if (row_n > self.getDataSize()):
            raise AttributeError("Row number doesn't exist")
        return self.data[row_n].split(self.delimiter)
