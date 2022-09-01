import math

def is_prime(n):
	for i in range(2, n // 2 + 1):
		if (n % i == 0):
			return False
			return True

def sieve(n):
	primes = [True] * (n+1)
	primes[0] = primes[1] = False

	for x in range(4,n+1,2):
		primes[x] = False

		for x in range(3,int(math.sqrt(n))+1,2):
			if(primes[x]):
				for y in range(x*x,n+1,x):
					primes[y] = False

					return primes