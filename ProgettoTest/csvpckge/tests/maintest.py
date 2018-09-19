from csvConvtestBB import TestCsvConverter
import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCsvConverter)
    unittest.TextTestRunner(verbosity=2).run(suite)
