import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    Class to test the functions on the readfiles module

    Args:
        unittest.TestCase: Class from the uniitest module to create unit test
    """

    def test_get_data(self):
        with open("test.txt", 'r') as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file('test.txt'))

    def test_nonfile(self):
        self.assertEqual(None, readfiles.read_file('tests.txt'))


    if __name__ == "__main__":
        unittest.main()