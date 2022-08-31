# Special Pythagorean triplet
# https://projecteuler.net/problem=9
# a + b + c = 1000
# a^2 + b^2 = c^2
def special_pythagorean_triplet():
	a = b = c = 0
	s = 1000
	for a in range(1, s // 3):
		for b in range(a, s // 2):
			c = s - a - b
			if (a * a + b * b == c * c):
				return a * b * c

if __name__ == '__main__':
	print(special_pythagorean_triplet())