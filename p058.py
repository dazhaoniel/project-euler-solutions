# Spiral primes
# https://projecteuler.net/problem=58
from lib import is_prime

def spiral_primes():
	n = 1
	prime_count = 0
	total = 1
	while True:
		# a = (n+2)**2 no need to check, never going to be prime
		prime_count += is_prime((n+2)**2-3*n-3)
		prime_count += is_prime((n+2)**2-2*n-2)
		prime_count += is_prime((n+2)**2-n-1)
		total += 4
		n += 2
		if (prime_count/total < 0.1):
			return n

if __name__ == '__main__':
	print(spiral_primes())


