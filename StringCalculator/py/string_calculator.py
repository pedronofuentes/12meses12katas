def add(numbers):
	numbers_list = []
	if numbers.find('//') == 0:
		numbers_list = [int(x) for x in numbers[4:].split(numbers[2])]
	else:
		numbers_list = [int(y) for x in numbers.split('\n') if x for y in x.split(',')]

	negative_numbers = [x for x in numbers_list if x < 0]
	if negative_numbers:
		raise ValueError('Negative numbers are not allowed: %s' % ','.join(['%i' % x for x in negative_numbers]))

	return sum(numbers_list)