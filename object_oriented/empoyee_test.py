import unittest
from oop import Employee


class employeesTest(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp1 = Employee('Marvin', 'Sakali', 50000)
        self.emp2 = Employee('Mercy', 'Wekesa', 40000)

    def tearDown(self):
        print('tearDown\n')

    def test_fullname(self):
        print('Test_fullname')
        self.assertEqual(self.emp1.full_name, 'Marvin Sakali')
        self.assertEqual(self.emp2.full_name, 'Mercy Wekesa')

        self.emp1.first = "Val"
        self.emp2.last = "Wekesa"

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'Marvin.Sakali@company.com')
        self.assertEqual(self.emp2.email, "Mercy.Wekesa@company.com")

    def test_pay(self):
        print('test_pay')
        self.assertEqual(self.emp1.pay, 50000)
        self.assertEqual(self.emp2.pay, 40000)

    def test_apply_raise(self):
        print('test_apply_raise')
        self.assertEqual(self.emp1.pay, 50000)
        self.assertEqual(self.emp2.pay, 40000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52000)
        self.assertEqual(self.emp2.pay, 41600)


if __name__ == "__main__":
    unittest.main()
