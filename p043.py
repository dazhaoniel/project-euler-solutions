# Sub-string divisibility
# https://projecteuler.net/problem=43
from itertools import permutations

def substring_divisibility():
	p = permutations('0123456789')

	s = 0
	for n in list(p):
		if (int(''.join(n[1:4])) % 2 == 0
		and int(''.join(n[2:5])) % 3 == 0
		and int(''.join(n[3:6])) % 5 == 0
		and int(''.join(n[4:7])) % 7 == 0
		and int(''.join(n[5:8])) % 11 == 0
		and int(''.join(n[6:9])) % 13 == 0
		and int(''.join(n[7:10])) % 17 == 0):
			s += int(''.join(n))

	return s


if __name__ == '__main__':
	print(substring_divisibility())