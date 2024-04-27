import unittest
from unittest.mock import patch
from io import StringIO
from alphabet.alphabet import main

class AlphabetTestCase(unittest.TestCase):
    def test_main(self):
        # Existing test cases...

        # Test case 7: num = 10
        with patch('builtins.input', return_value='10'):
            expected_output = '      A\n    B C\n  D E F\nG H I J\n'
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                self.assertEqual(fake_output.getvalue(), expected_output)

        # Test case 8: num = 15
        with patch('builtins.input', return_value='15'):
            expected_output = '        A\n      B C\n    D E F\n  G H I J\nK L M N O\n'
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                self.assertEqual(fake_output.getvalue(), expected_output)

        with patch('builtins.input', return_value='21'):
            expected_output = '          A\n        B C\n      D E F\n    G H I J\n  K L M N O\nP Q R S T U\n'
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
