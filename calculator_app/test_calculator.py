import unittest
import calculator


class testCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 5), 10)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(1, -1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(1, -1), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 5), 10)
        self.assertEqual(calculator.multiply(-1, -1), 1)
        self.assertEqual(calculator.multiply(1, -1), -1)

    def test_divide(self):
        self.assertEqual(calculator.divide(4, 2), 2)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(1, -1), -1)

    def test_square(self):
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.square(-2), 4)
        self.assertEqual(calculator.square(0), 0)


if __name__ == '__main__':
    unittest.main()
