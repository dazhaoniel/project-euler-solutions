# Highly divisible triangular number
# https://projecteuler.net/problem=12
import math

def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n) + 1)) if not n % i)

def triangle(n):
    return ((n ** 2) + n) // 2

def find_triangle_number():
	i = 1
	c = 1
	while (c <= 500):
		n = triangle(i)
		c = get_factors(n)
		i += 1
	return n

if __name__ == '__main__':
	print(find_triangle_number())