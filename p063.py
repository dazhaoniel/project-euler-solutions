# Powerful digit counts
# https://projecteuler.net/problem=63
def powerful_digit_counts():
	c = 0
	for i in range(1, 10):
		p = 1
		while True:
			if p == len(str(i**p)):
				c += 1
			else:
				break
			p += 1

	return c


if __name__ == '__main__':
	print(powerful_digit_counts())