# Pentagon numbers
# https://projecteuler.net/problem=44
from lib import is_pentagon
	
def pentagon_numbers():
	i = 1
	while True:
		for j in range(1, i):
			a = i*(3*i-1)/2
			b = j*(3*j-1)/2
			if is_pentagonal(a+b) and is_pentagonal(a-b):
				return a-b
		i += 1


if __name__ == '__main__':
	print(pentagon_numbers())
