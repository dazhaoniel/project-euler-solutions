# Even Fibonacci numbers
# https://projecteuler.net/problem=2
def even_fib_numbers():
	s = 2
	x = 1
	y = 2
	while y <= 4000000:
		x, y = y, x + y
		if x%2 == 0:
			s += x

	return s


if __name__ == '__main__':
	print(even_fib_numbers())