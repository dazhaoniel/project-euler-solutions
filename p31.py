# Coin sums
# https://projecteuler.net/problem=31
def coin_sums():
	target = 200
	ways = [1] + [0] * target
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	for coin in coins:
		for i in range(coin, target + 1):
			ways[i] += ways[i - coin]
	return ways[target]

if __name__ == '__main__':
	print(coin_sums())