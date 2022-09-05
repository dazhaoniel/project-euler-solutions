# Prime permutations
# https://projecteuler.net/problem=49
from lib import prime3
from itertools import permutations

def prime_permutations():
	temp = prime3(10000)
	primes = [i for i in temp if len(str(i)) == 4]

	for a in primes:
		p = permutations(str(a))
		numbers = [int(''.join(x)) for x in list(p)]
		for b in numbers:
			d = b-a
			c = b+d
			if c in primes and b in primes and c in numbers and a < b < c and a > 1487:
				# print(a, b, c)
				return str(a)+str(b)+str(c)



if __name__ == '__main__':
	print(prime_permutations())