def add(numbers):
	if not numbers:
		return 0

	result = 0
	for x in numbers.split(','):
		result += int(x)

	return result