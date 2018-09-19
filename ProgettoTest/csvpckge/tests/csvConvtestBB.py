import unittest
from ..csvop.CsvDataConverter import CsvDataConverter

class TestCsvConverter(unittest.TestCase):

    def testRowVuoto(self):
        row = []
        elemtypes = ["INT", "DOUBLE"]
        with self.assertRaises(ValueError) as fail:
            conv = CsvDataConverter(row, elemtypes)

    def testElemVuoto(self):
        row = ["3", "4.0"]
        elemtypes = []
        with self.assertRaises(ValueError) as fail:
            conv = CsvDataConverter(row, elemtypes)

    def testLunghezze(self):
        row = ["6", "4"]
        elemtypes = ["INT", "VARCHAR(256)", "DATE"]
        with self.assertRaises(ValueError) as fail:
            conv = CsvDataConverter(row, elemtypes)

    def testElementinonContenuti(self):
        row = ["3", "stringa", "4.0", "1994-04-03"]
        elemtypes = ["INT", "TEXT", "DOUBLE", "TIME"]
        conv = CsvDataConverter(row, elemtypes)
        final = "%s,%s" % (row[0], row[2])
        self.assertEqual(conv.values2Query(), final)

    def testElementiCorretti(self):
        row = ["3", "stringa", "4.0", "1994-04-03"]
        elemtypes = ["INT", "VARCHAR(256)", "DOUBLE", "DATE"]
        conv = CsvDataConverter(row, elemtypes)
        final = "%s,\"%s\",%s,%s%s" % (row[0], row[1], row[2], row[3], CsvDataConverter.TIME)
        self.assertEqual(conv.values2Query(), final)
