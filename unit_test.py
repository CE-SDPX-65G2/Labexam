import unittest

from app import app

class AppTestCase(unittest.TestCase):

    def test_false_when_x_is_0(self):
        self.assertEqual(eval(app.check_num(0)), False)
    def test_false_when_x_is_3(self):
        self.assertEqual(eval(app.check_num(3)), False)
    def test_true_when_x_is_neg5(self):
        self.assertEqual(eval(app.check_num(-5)), True)
        
if __name__ == "__main__":
    unittest.main()
