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

	def test_add_unknown_amount_of_numbers(self):
		self.assertEqual(string_calculator.add('1,3,5,8'), 17, 'add("1,3,5,8") == 17')
		self.assertEqual(string_calculator.add('2,3,4,5,6'), 20, 'add("2,3,4,5,6") == 20')

	def test_new_line_separator(self):
		self.assertEqual(string_calculator.add('1\n2,3'), 6, 'add(1\\n2,3) == 6')
		self.assertEqual(string_calculator.add('1\n2,3\n5'), 11, 'add(1\\n2,3\\n5) == 11')


if __name__ == '__main__':
	unittest.main()