"""
A simple calculator class for basic arithmetic operations.
"""

import unittest

class Calculator:
    """
    A class for performing basic arithmetic operations.
    """

    def add(self, x_value, y_value):
        """
        Add two numbers and return the result.

        Args:
            x_value (float or int): The first number.
            y_value (float or int): The second number.

        Returns:
            float or int: The sum of x_value and y_value.
        """
        return x_value + y_value

    def subtract(self, x_value, y_value):
        """
        Subtract the second number from the first and return the result.

        Args:
            x_value (float or int): The first number.
            y_value (float or int): The second number.

        Returns:
            float or int: The result of subtracting y_value from x_value.
        """
        return x_value - y_value

    def multiply(self, x_value, y_value):
        """
        Multiply two numbers and return the result.

        Args:
            x_value (float or int): The first number.
            y_value (float or int): The second number.

        Returns:
            float or int: The product of x_value and y_value.
        """
        return x_value * y_value

    def divide(self, x_value, y_value):
        """
        Divide the first number by the second and return the result.

        Args:
            x_value (float or int): The numerator.
            y_value (float or int): The denominator.

        Returns:
            float: The result of dividing x_value by y_value.

        Raises:
            ValueError: If y_value is zero.
        """
        if y_value == 0:
            raise ValueError("Division by zero is not allowed")
        return x_value / y_value


class CalculatorTest(unittest.TestCase):
    """
    A test case class for the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """
        Test the add method.
        """
        self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        """
        Test the subtract method.
        """
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        """
        Test the multiply method.
        """
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        """
        Test the divide method.
        """
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()
