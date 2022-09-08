# Large non-Mersenne prime
# https://projecteuler.net/problem=97
def large_non_mersenne_prime():
	return (28433 * pow(2, 7830457, 10 ** 10) + 1) % 10 ** 10

if __name__ == '__main__':
	print(large_non_mersenne_prime())