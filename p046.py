# Goldbach's other conjecture
# https://projecteuler.net/problem=46
import math
from lib import is_prime

def goldbachs():
	i = 3
	primes = [2]

	while True:
		if is_prime(i):
			primes.append(i)
		else:
			flag = False
			for p in primes:
				if math.sqrt((i-p)/2) == int(math.sqrt((i-p)/2)):
					flag = True
					break
			if flag == False:
				return i
		i += 2


if __name__ == '__main__':
	print(goldbachs())

