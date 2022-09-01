# Counting summations
# https://projecteuler.net/problem=76
def counting_summations():
	target = 100
	ways = [1] + [0] * target
	for i in range(1, target):
		for j in range(i, target + 1):
			ways[j] += ways[j - i]

	return ways[target]


if __name__ == '__main__':
	print(counting_summations())