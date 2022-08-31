# Factorial digit sum
# https://projecteuler.net/problem=20
def factorial_digit_sum():
	n = 1
	for i in range(100, 0, -1):
		n *= i
	
	s = 0

	for char in str(n):
		s += int(char)

	return s



if __name__ == '__main__':
	print(factorial_digit_sum())
