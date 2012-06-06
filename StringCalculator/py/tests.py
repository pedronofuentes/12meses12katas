import string_calculator
import unittest

class StringCalculatorTest(unittest.TestCase):
	def test_add_empty_string(self):
		self.assertEqual(string_calculator.add(''), 0, 'add("") == 0')

	def test_add_one_number(self):
		self.assertEqual(string_calculator.add('1'), 1, 'add("1") == 1')
		self.assertEqual(string_calculator.add('6'), 6, 'add("6") == 6')

	def test_add_two_numbers(self):
		self.assertEqual(string_calculator.add('1,2'), 3, 'add("1,2") == 3')
		self.assertEqual(string_calculator.add('5,3'), 8, 'add("5,3") == 8')


if __name__ == '__main__':
	unittest.main()