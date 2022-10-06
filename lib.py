import math
import numpy as np

def is_prime(n):
	if n == 1: return False 
	if n == 2: return True 
	for i in range(3, int(n**0.5)+1, 2):
		if (n % i == 0):
			return False
	return True


def prime3(upto=1000000):
	return [2] + list(filter(lambda num: (num % np.arange(3,1+int(math.sqrt(num)),2)).all(), range(3,upto+1,2)))


def is_prime2(n):
    return not any(n % x == 0 for x in range(2, int(n**0.5)+1))


def is_pentagonal(n):
	return (1+(24*n+1)**0.5) % 6 == 0


def is_hexagonal(n):
	return (1+(8*n+1)**0.5) % 4 == 0