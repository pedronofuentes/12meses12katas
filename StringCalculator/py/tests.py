import string_calculator
import unittest

class StringCalculatorTest(unittest.TestCase):
	def test_add_empty_string(self):
		self.assertEqual(string_calculator.add(''), 0, 'add("") == 0')

	def test_add_one_number(self):
		self.assertEqual(string_calculator.add('1'), 1, 'add("1") == 1')

	def test_add_two_numbers(self):
		self.assertEqual(string_calculator.add('1,2'), 3, 'add("1,2") == 3')


if __name__ == '__main__':
	unittest.main()