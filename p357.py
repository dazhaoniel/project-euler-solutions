# Prime generating integers
# https://projecteuler.net/problem=357
import math
from lib import is_prime2

# def divisor_generator(n):
# 	'''Generates the divisiors of input num'''
# 	large_divisors = []
# 	for i in range(1, int(math.sqrt(n) + 1)):
# 		if n % i == 0:
# 			yield i
# 			if i*i != n:
# 				large_divisors.append(n / i)
# 	for divisor in reversed(large_divisors):
# 		yield divisor

def prime_generating_integers():
	limit = 100000000
	answer = []
	for n in range(1, limit + 1):
		# divisors_list = list(divisor_generator(n))
		if all(n%d != 0 or is_prime2(d+n//d) for d in range(1, int(math.sqrt(n) + 1))):
			answer.append(n)
	return sum(answer)


if __name__ == '__main__':
	print(prime_generating_integers())

