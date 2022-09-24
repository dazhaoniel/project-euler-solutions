# Path sum: two ways
# https://projecteuler.net/problem=81
def path_sum_two_ways():
	f = open('./p081_matrix.txt')
	numbers = [list(map(int, line.strip().split(','))) for line in f.readlines()]
	n = len(numbers)

	# initialize the first row
	for i in range(1, n):
		numbers[0][i] += numbers[0][i-1]
	# initialize the first column
	for i in range(1, n):
		numbers[i][0] += numbers[i-1][0]
	
	for i in range(1, n):
		for j in range(1, n):
			numbers[i][j] += min(numbers[i-1][j], numbers[i][j-1])

	return numbers[n-1][n-1]



if __name__ == '__main__':
	print(path_sum_two_ways())