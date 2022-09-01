# Circular primes
# https://projecteuler.net/problem=35
import numpy as np
import math

# http://rebrained.com/?p=458
def prime3(upto=1000000):
	return [2] + list(filter(lambda num: (num % np.arange(3,1+int(math.sqrt(num)),2)).all(), range(3,upto+1,2)))

def rotation(number):
	str_number = str(number)
	return {
	int(str_number[i:] + str_number[:i])
	for i in range(len(str_number))
	}

def circular_primes():
	count = 0
	prime = prime3()
	for i in prime:
		count += 1
		numbers_list = list(rotation(i))
		for num in numbers_list:
			if num not in prime:
				count -= 1
				break

	return count

if __name__ == '__main__':
	print(circular_primes())