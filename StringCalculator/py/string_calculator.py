def add(numbers):
	if numbers.find('//') == 0:
		return sum([int(x) for x in numbers[4:].split(numbers[2])])

	return sum([int(y) for x in numbers.split('\n') if x for y in x.split(',')])