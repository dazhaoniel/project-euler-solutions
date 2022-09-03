# Summation of primes
# https://projecteuler.net/problem=10
def summation_of_primes():
	# use list comprehension
	primes = [x for x in range(2, 2000001) if is_prime(x)]
	s = sum(primes)
	return s

if __name__ == '__main__':
	print(summation_of_primes())