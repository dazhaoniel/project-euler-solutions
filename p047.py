# Distinct primes factors
# https://projecteuler.net/problem=47
from lib import prime3

def npf(n, primes):
	c = 0
	for p in primes:
		if p*p > n:
			c += 1
			return c

		pf = False
		while (n % p == 0):
			pf = True
			n = n / p;

		if pf:
			c += 1

		if n == 1:
			return c

def distinct_prime_factors():
	n = 2*3*5*7
	primes = prime3()

	while True:
		if npf(n, primes) == 4:
			n += 1
			if npf(n, primes) == 4:
				n += 1
				if npf(n, primes) == 4:
					n += 1
					if npf(n, primes) == 4:
						return n-3
		n += 1


if __name__ == '__main__':
	print(distinct_prime_factors())

