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
            self.assertEqual(filtered_print_output[4], 'Arkdba')
            self.assertEqual(filtered_print_output[5], 'baaar')
            self.assertEqual(filtered_print_output[6], 'arbadakarbA')
            self.assertEqual(filtered_print_output[7], 'abdkrA')
            self.assertEqual(filtered_print_output[8], '11')

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
            self.assertEqual(filtered_print_output[4], 'Hlo')
            self.assertEqual(filtered_print_output[5], 'el')
            self.assertEqual(filtered_print_output[6], 'olleH')
            self.assertEqual(filtered_print_output[7], 'olH')
            self.assertEqual(filtered_print_output[7], '5')

    @patch('sys.stdout', new_callable=StringIO)
    def test_qwertyuiop(self, stdout):
        with patch('builtins.input', return_value='qwertyuiop'):
            runpy = imp.load_source('__main__', './slices.py')

            print_output = stdout.getvalue().split('\n')
            filtered_print_output = [x for x in print_output if x]
            self.assertEqual(len(filtered_print_output), 9)
            self.assertEqual(filtered_print_output[0], 'e')
            self.assertEqual(filtered_print_output[1], 'o')
            self.assertEqual(filtered_print_output[2], 'qwert')
            self.assertEqual(filtered_print_output[3], 'qwertyui')
            self.assertEqual(filtered_print_output[4], 'qetuo')
            self.assertEqual(filtered_print_output[5], 'wryip')
            self.assertEqual(filtered_print_output[6], 'poiuytrewq')
            self.assertEqual(filtered_print_output[7], 'piyrw')
            self.assertEqual(filtered_print_output[8], '10')


if __name__ == '__main__':
    unittest.main()
