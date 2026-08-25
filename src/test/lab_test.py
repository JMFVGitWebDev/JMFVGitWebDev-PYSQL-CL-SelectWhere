import unittest

from src.main.user import User
from src.main.lab import problem1, problem2


class LabTest(unittest.TestCase):
    def test_problem1_get_all_smiths(self):
        """
        This test calls the problem1 function and then compares it to the hardcoded list here, if they are the
        same then the test passes.
        """
        expected_result = [
            User(2, "Alexa", "Smith", 42500.00),
            User(4, "Brandon", "Smith", 120000.00),
        ]

        actual_result = problem1()

        self.assertEqual(expected_result, actual_result)

    def test_problem2_salary_greater_than(self):
        """
        This test calls the problem2 function and then compares it to the hardcoded list here, if they are the
        same then the test passes. Note the seed data includes an employee at exactly $75000 - that employee
        must NOT appear here, since 75000 is not "greater than" 75000. This is what actually catches a ">="
        mistake.
        """
        expected_result = [
            User(3, "Steve", "Jones", 99890.99),
            User(4, "Brandon", "Smith", 120000.00),
        ]

        actual_result = problem2()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
