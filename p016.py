# Power digit sum
# https://projecteuler.net/problem=16
def power_digit_sum():
	num = 2 ** 1000
	return sum([int(char) for char in str(num)])


if __name__ == '__main__':
	print(power_digit_sum())