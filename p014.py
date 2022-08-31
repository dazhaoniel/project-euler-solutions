# Longest Collatz sequence
# https://projecteuler.net/problem=14
def collatz(n):
	# n → n/2 (n is even)
	# n → 3n + 1 (n is odd)
	if (n % 2 == 0):
		return n // 2
	return n * 3 + 1

def longest_collatz():
	# store traversed list in dictionary
	d = {}

	for i in range(2, 1000000):
		l = 1
		n = i
		while (n != 1):
			if (n in d):
				l = l + d[n] - 1
				break
			num = collatz(n)
			l += 1
			n = num
		
		d[i] = l

	return max(d, key=d.get)

if __name__ == '__main__':
	print(longest_collatz())