# Palindromic sums
# https://projecteuler.net/problem=125
import math

def is_palindrome(n):
	if list(str(n)) == list(str(n))[::-1]:
		return True
	return False

def palindromic_sums():
	# generate all palindromic numbers and sum them
	limit = 10**8
	sqrt_limit = int(math.sqrt(limit))
	unique_list = set([])

	for i in range(1, sqrt_limit):
		n = i**2
		for j in range(i+1, sqrt_limit):
			n += j**2
			if n>limit:
				break
			if is_palindrome(n):
				unique_list.add(n)

	return sum(unique_list)

if __name__ == '__main__':
	print(palindromic_sums())
