import unittest

from temp import convert_temp


class TestConversion(unittest.TestCase):

    def test_conversion_case_1(self):
        self.assertEqual(convert_temp(0, from_temp='Celsius'), 32)
    
    def test_conversion_case_2(self):
        self.assertEqual(convert_temp(10, from_temp='Celsius'), 50)

    def test_conversion_case_3(self):
        self.assertEqual(convert_temp(32, from_temp='Fahrenheit'), 0)

    def test_celsius_cant_be_below_limit(self):
        self.assertEqual(convert_temp(-273.16, from_temp='Celsius'), 'Invalid temperature')
        

if __name__ == '__main__':
    unittest.main()