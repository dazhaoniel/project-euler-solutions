# Singular integer right triangles
# https://projecteuler.net/problem=75
from math import sqrt, gcd

def singular_inter_right_triangles():
	# https://en.wikipedia.org/wiki/Pythagorean_triple
	# a**2 + b**2 = c**2 and a, b, and c are coprime
	# generating the triplets m > n > 0
	# a = m**2 - n**2
	# b = 2*m*n
	# c = m**2 + n**2
	limit = 1500000
	triangles = [0]*1500000
	for m in range(2, int(sqrt(limit))):
		for n in range(1, m):
			if (((n + m) % 2) == 1 and gcd(m, n) == 1):
				a = m**2 - n**2
				b = 2*m*n
				c = m**2 + n**2
				p = a+b+c
				while p < limit:
					triangles[p] += 1
					p += a+b+c
	return triangles.count(1)

if __name__ == '__main__':
	print(singular_inter_right_triangles())