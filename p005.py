# Smallest multiple
# https://projecteuler.net/problem=5
import math
from functools import reduce

def lcm(a, b):
	return a * b // math.gcd(a, b)

def smallest_multiple():
	return reduce(lcm, range(1, 20+1))


if __name__ == '__main__':
	print(smallest_multiple())