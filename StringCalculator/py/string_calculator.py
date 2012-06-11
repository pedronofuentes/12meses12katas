def add(numbers):
	numbers_list = [int(x) for x in numbers.split(',') if x]

	return sum(numbers_list)