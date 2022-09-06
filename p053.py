# Combinatoric selections
# https://projecteuler.net/problem=53
from math import factorial as f

def ncr(n, r):
	return f(n)/(f(r)*f(n-r))

def combinatoric_selections():
	c = 0
	for n in range(23, 101):
		for r in range(4, n-1):
			if ncr(n, r) > 1000000:
				c += 1
	return c

if __name__ == '__main__':
	print(combinatoric_selections())