def add(numbers):
	numbers_list = [int(y) for x in numbers.split('\n') if x for y in x.split(',')]

	return sum(numbers_list)