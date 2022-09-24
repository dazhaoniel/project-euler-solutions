# Largest exponential
# https://projecteuler.net/problem=99
from math import log10

def largest_exponential():
	f = open('./p099_base_exp.txt')
	answer = largest = 0
	count = 1
	for line in f.readlines():
		a, b = list(map(int, line.split(',')))
		# log(a) ** x = x * log(a)
		if b * log10(a) > largest:
			largest = b * log10(a)
			answer = count
		count += 1

	return answer


if __name__ == '__main__':
	print(largest_exponential())