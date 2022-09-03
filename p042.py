# Coded triangle numbers
# https://projecteuler.net/problem=42
import math

def is_triangle(n):
	# https://www.mathworks.com/matlabcentral/answers/47533-best-way-to-determine-if-number-is-triangular-number
	return math.sqrt(8 * n + 1) == int(math.sqrt(8 * n + 1))

def coded_triangle_numbers():
	words = open('./p042_words.txt').read().replace('\"', '').split(',')
	c = 0
	for w in words:
		s = 0
		for char in w:
			s += ord(char) - 64
		if is_triangle(s):
			c += 1

	return c


if __name__ == '__main__':
	print(coded_triangle_numbers())