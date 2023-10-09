import unittest
from employee import Employee


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_employee = Employee('Ash', 'Liu')

    def test_give_default_raise(self):
        self.assertEqual(self.new_employee.annual_salary, 5000)

    def test_give_custom_raise(self):
        self.new_employee.give_raise(10000)
        self.assertEqual(self.new_employee.annual_salary, 15000)


if __name__ == '__main__':
    unittest.main()
