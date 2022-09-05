# Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45
from lib import is_pentagonal, is_hexagonal

def tph():
	i = 286
	while True:
		t = i*(i+1)/2
		if is_pentagonal(t) and is_hexagonal(t):
			return t
		i += 1

if __name__ == '__main__':
	print(tph())
