import unittest

from app import app

class AppTestCase(unittest.TestCase):


    def test_true_when_x_is_13219(self):
        self.assertEqual(app.is_prime(13219), "True")

    def test_False_when_x_is_17(self):
        self.assertEqual(app.is_prime(36), "True")
    

if __name__ == "__main__":
    unittest.main()
