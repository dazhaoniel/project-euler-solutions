# Prime pair sets
# https://projecteuler.net/problem=60
import itertools
from lib import prime3

primes = prime3(10000)

# check prime pairs
def cpp(l):
	for p in itertools.permutations(l, 2):
		n = p[0]*(10**len(str(p[1])))+p[1]
		if n not in primes:
			return False
	return True

def prime_pair_sets():
	for a in primes:
		for b in primes:
			if b < a:
				continue
			if cpp([a, b]):
				for c in primes:
					if c < b:
						continue
					if cpp([a, b, c]):
						for d in primes:
							if d < c:
								continue
							if cpp([a, b, c, d]):
								for e in primes:
									if e < d:
										continue
									print(a,b,c,d,e)
									if cpp([a, b, c, d, e]):
										return sum([a,b,c,d,e])



if __name__ == '__main__':
	print(prime_pair_sets())