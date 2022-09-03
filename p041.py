# Pandigital prime
# https://projecteuler.net/problem=41
from lib import prime3

def pandigital_prime():
	# https://stackoverflow.com/questions/2081030/tips-to-solve-problem-41-of-project-euler/27891197#27891197
	# 7! number
	primes = prime3(7654321)
	largest = 0

	for n in primes:
		s = list(str(n))
		s.sort()
		if s == [str(i) for i in range(1, len(s) + 1)]:
			if n > largest:
				largest = n

	return largest


if __name__ == '__main__':
	print(pandigital_prime())