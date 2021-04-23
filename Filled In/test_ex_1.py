import unittest

class TestLen(unittest.TestCase):

    def test_length_of_list(self):
        self.assertEqual(len([1, 3, 4, 1, 3]), 5)
        
    def test_length_of_string(self):
        self.assertEqual(len("hello world"), 11)
    
    def test_hello(self):
        self.assertEqual(True, True)
        
        
if __name__ == '__main__':
    unittest.main()