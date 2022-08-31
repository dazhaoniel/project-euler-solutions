# Pandigital products
# https://projecteuler.net/problem=32
def pandigital_products():
	num = set('123456789')
	answer = set()
	# x is 1 digit and y is 4 digits
	for x in range(1, 10):
		for y in range(1000, 10000):
			s = str(x) + str(y) + str(x * y)
			if len(s) != 9: break
			if (set(s) == num): answer.add(x * y)

	# x is 2 digits and y is 3 digits
	for x in range(10, 100):
		for y in range(100, 1000):
			s = str(x) + str(y) + str(x * y)
			if len(s) != 9: break
			if (set(s) == num): answer.add(x * y)

	return sum(answer)


if __name__ == '__main__':
	print(pandigital_products())