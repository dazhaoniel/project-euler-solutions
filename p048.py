# Self powers
# https://projecteuler.net/problem=48
def self_powers():
	s = 0
	for i in range(1, 1001):
		s += i ** i

	return str(s)[-10:]


if __name__ == '__main__':
	print(self_powers())