# Lattice paths
# https://projecteuler.net/problem=15
import math

def nck(n, k):
	# https://en.wikipedia.org/wiki/Binomial_coefficient
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def lattice_paths():
	return nck(20 + 20, 20)


if __name__ == '__main__':
	print(lattice_paths())