import unittest

from unittest.mock import patch, Mock

from hn_api import get_top_stories


class TestCacher(unittest.TestCase):

    @patch('hn_api.requests')
    def test_gets_from_api_no_cache(self, requests):
        expected_data = [9129911, 9129199, 9127761, 9128141, 9128264, 9127792, 9129248, 9127092, 9128367]
        requests.get.return_value.json.return_value = expected_data
        self.assertEqual(get_top_stories(), expected_data)
        requests.get.assert_called_once_with('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
        requests.get.return_value.json.assert_called_once_with()
        
    @patch('hn_api.CACHE_DATABASE', {'data': [123, 14, 15]})
    @patch('hn_api.requests')
    def test_gets_from_cache(self, requests):
        self.assertEqual(get_top_stories(), [123, 14, 15])
        self.assertEqual(requests.get.called, False)
 
        
if __name__ == '__main__':
    unittest.main()