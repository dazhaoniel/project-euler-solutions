# Lychrel numbers
# https://projecteuler.net/problem=55
def is_lychrel(n):
	for i in range(50):
		s = n + int(str(n)[::-1])
		if str(s) == str(s)[::-1]:
			return False
		n = s
	return True


def lychrel_numbers():
	c = 0
	for i in range(1, 10001):
		if is_lychrel(i):
			c += 1
	return c


if __name__ == '__main__':
	print(lychrel_numbers())