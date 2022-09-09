# Maximum path sum II
# https://projecteuler.net/problem=67
def maximum_path_sum_ii():
	f = open('./p067_triangle.txt')
	numbers = [line.replace('\n', '') for line in f.readlines()]
	for i in range(len(numbers)):
		numbers[i] = [int(x) for x in numbers[i].strip().split(' ')]

	# bottom up approach as in problem 18
	# from len()-2 (second last) row, adds the max of the bottom 2
	for i in range(len(numbers)-2, -1, -1):
		for j in range(len(numbers[i])):
			numbers[i][j] = numbers[i][j] + max(numbers[i+1][j], numbers[i+1][j+1])

	return numbers[0][0]


if __name__ == '__main__':
	print(maximum_path_sum_ii())