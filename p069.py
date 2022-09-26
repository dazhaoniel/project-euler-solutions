# Totient maximum
# https://projecteuler.net/problem=69
from lib import prime3

def totient_maximum():
	# https://en.wikipedia.org/wiki/Euler's_totient_function
	# relative prime means the only positive integer that is a divisor of both of them is 1
	primes = prime3(100)
	answer = 1
	for p in primes:
		if p*answer < 1000000:
			answer *= p
	return answer


if __name__ == '__main__':
	print(totient_maximum())
