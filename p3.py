# Largest prime factor
# https://projecteuler.net/problem=3
import math

def largest_prime_factor(n):
	while n % 2 == 0:
		n = n / 2

	for i in range(3, int(math.sqrt(n)), 2):
		# while i divides n, print i and divide n
		while n % i == 0:
			n = n / i

	return i

if __name__ == '__main__':
	print(largest_prime_factor(600851475143))