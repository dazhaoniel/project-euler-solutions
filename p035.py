# Circular primes
# https://projecteuler.net/problem=35
from lib import is_prime

def rotation(number):
    str_number = str(number)
    return {
        int(str_number[i:] + str_number[:i])
        for i in range(len(str_number))
    }

def circular_primes():
	count = 0
	
	for i in range(2, 1000000):
		if is_prime(i):
			count += 1
			numbers_list = list(rotation(i))
			for num in numbers_list:
				if not is_prime(num):
					count -= 1
					break

	return count

if __name__ == '__main__':
	print(circular_primes())