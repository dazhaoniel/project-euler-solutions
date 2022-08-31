# 10001st prime
# https://projecteuler.net/problem=7
from lib import is_prime

def find_prime():
	count = 1
	n = 3
	while n > 0:
		if is_prime(n):
			count += 1
		if (count == 10001):
		 	return n
		n += 1

if __name__ == '__main__':
	print(find_prime())