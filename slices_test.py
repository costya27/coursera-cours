import contextlib
import io
from unittest.mock import patch
import imp
import unittest
from io import StringIO

from slices import test_func


class TestingSlices(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_abracadabra(self, stdout):
        with patch('builtins.input', return_value='Abrakadabra'):
            runpy = imp.load_source('__main__', './slices.py')

            print_output = stdout.getvalue().split('\n')
            filtered_print_output = [x for x in print_output if x]
            self.assertEqual(len(filtered_print_output), 9)
            self.assertEqual(filtered_print_output[0], 'r')
            self.assertEqual(filtered_print_output[1], 'r')
            self.assertEqual(filtered_print_output[2], 'Abrak')
            self.assertEqual(filtered_print_output[3], 'Abrakadab')

    @patch('sys.stdout', new_callable=StringIO)
    def test_hello(self, stdout):
        with patch('builtins.input', return_value='Hello'):
            runpy = imp.load_source('__main__', './slices.py')

            print_output = stdout.getvalue().split('\n')
            filtered_print_output = [x for x in print_output if x]
            self.assertEqual(len(filtered_print_output), 9)
            self.assertEqual(filtered_print_output[0], 'l')
            self.assertEqual(filtered_print_output[1], 'l')
            self.assertEqual(filtered_print_output[3], 'Hel')

    def test_test_func(self):
        res = test_func(2,3)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
