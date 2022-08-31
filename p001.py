# Multiples of 3 or 5
# https://projecteuler.net/problem=1
def find_multiples():
	s = 0
	for x in range(1000):
		if x%3 == 0 or x%5 == 0:
			s += x

	return s


if __name__ == '__main__':
	print(find_multiples())