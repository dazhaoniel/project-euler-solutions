# Number spiral diagonals
# https://projecteuler.net/problem=28
def number_spiral_diagonals():
	sum = 1
	n = 1
	while ((n + 2) ** 2 <= 1001 * 1001):
		sum += (n + 2) ** 2 * 4 - (n + 1) * 6
		n += 2
	return sum


if __name__ == '__main__':
	print(number_spiral_diagonals())