# Powerful digit sum
# https://projecteuler.net/problem=56
def powerful_digit_sum():
	s = 0
	for a in range(100):
		for b in range(100):
			t = sum([int(x) for x in str(a**b)])
			if (t > s):
				s = t
	return s

if __name__ == '__main__':
	print(powerful_digit_sum())