# Prime summations
# https://projecteuler.net/problem=77
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]

def prime_summations():
	L, target = 5000, 11
	while True:
		ways = [1] + [0] * target
		for p in primes:
			for i in range(p, target+1):
				ways[i] += ways[i-p]
		if ways[target] > L: break    
		target += 2

	return target

if __name__ == '__main__':
	print(prime_summations())