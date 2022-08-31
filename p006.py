# Sum square difference
# https://projecteuler.net/problem=6
def sum_square_difference():
	sum_of_square = sum(i ** 2 for i in range(1, 101))
	square_of_sum = sum(range(1, 101)) ** 2

	return square_of_sum - sum_of_square

if __name__ == '__main__':
	print(sum_square_difference())