# Square root convergents
# https://projecteuler.net/problem=57
def square_root_convergents():
	n = d = 1
	c = 0
	for i in range(1, 1000):
		a = n+2*d
		b = n+d
		if len(str(a)) > len(str(b)):
			c += 1
		n = a
		d = b

	return c

if __name__ == '__main__':
	print(square_root_convergents())