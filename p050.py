# Consecutive prime sum
# https://projecteuler.net/problem=50
from lib import prime3

def consecutive_prime_sum():
	# count and max value
	c = m = 0
	primes = prime3(1000000)

	for i in range(len(primes)):
		s = 0
		for j in range(i, len(primes)):
			s += primes[j]
			if s > 1000000:
				break
			if s in primes and j - i + 1 > c and s > m:
				c = j - i + 1
				m = s

	return c, m

if __name__ == '__main__':
	print(consecutive_prime_sum())