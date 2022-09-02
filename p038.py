# Pandigital multiples
# https://projecteuler.net/problem=38
def pandigital_multiples():
	pandigital = '123456789'
	largest = 0
	for i in range(1, 10000):
		target = ''
		# (1, 2, 3 ... n)
		n = 1
		
		while (len(target) < 9):
			target += str(n * i)
			n += 1

		t = ''.join(sorted(target))
		if (t == pandigital) and (int(target) > largest):
			largest = int(target)

	return largest


if __name__ == '__main__':
	print(pandigital_multiples())

