import unittest

from app import app

class AppTestCase(unittest.TestCase):

    def test_be_0_when_x_is_0(self):
        self.assertEqual(eval(app.num_divide_5(0)), 0)
    def test_be_15_when_x_is_3(self):
        self.assertEqual(eval(app.num_divide_5(3)), 15)
    def test_be_4dot5_when_x_is_1dot5(self):
        self.assertEqual(eval(app.num_divide_5(1.5)), 7.5)
        
if __name__ == "__main__":
    unittest.main()
