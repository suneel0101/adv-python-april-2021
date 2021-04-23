import unittest

from unittest.mock import patch

from lunch import get_lunch_recommendation, RESTAURANTS


class TestLunch(unittest.TestCase):

    @patch('lunch.random')
    def test_recommendation(self, random):
        # this is the output we expect
        expected_output = 'random lunch pick'

        # when random.choice is called, instead of using the built-in random
        # let's the fake version and force the output to be what we set above
        random.choice.return_value = expected_output

        # call the function, and check we get our expected output
        self.assertEqual(get_lunch_recommendation(), expected_output)

        # check that when we called the function, the function called random.choice and passed
        # in RESTAURANTS as the argument
        random.choice.assert_called_once_with(RESTAURANTS)
        
    @patch('lunch.random')
    @patch('lunch.RESTAURANTS', ['some list'])
    def test_restaurants_list_modular(self, random):
        expected_output = 'random lunch pick'
        random.choice.return_value = expected_output
        self.assertEqual(get_lunch_recommendation(), expected_output)
        random.choice.assert_called_once_with(['some list'])

    @patch('lunch.random')
    @patch('lunch.OUTPUT_FILE', 'test-recommendations.txt')
    def test_writes_to_file(self, random):
        expected_output = 'random lunch pick'
        random.choice.return_value = expected_output
        get_lunch_recommendation()

        # Checkif the file was written to
        with open('test-recommendations.txt', 'r') as f:
            text = f.read()
            self.assertEqual(text, 'random lunch pick')

        # Clean up the test file
        with open('test-recommendations.txt', 'w') as f:
            pass
 
if __name__ == '__main__':
    unittest.main()