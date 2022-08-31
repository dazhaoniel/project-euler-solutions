# Non-abundant sums
# https://projecteuler.net/problem=23
def is_abundant(n):
	sum_of_divisors = 1
	for i in range(2, (n // 2 + 1)):
		if n % i == 0:
			sum_of_divisors += i
	return sum_of_divisors > n

def non_abundant_sums():
	abundant_numbers = [n for n in range(12, 28124) if is_abundant(n)]
	abundant_sums = set()
	for i in abundant_numbers:
		for j in abundant_numbers:
			if (i + j > 28123):
				break
			else:
				abundant_sums.add(i+j)

	non_abundant_numbers = [q for q in range(28123) if q not in abundant_sums]
	return sum(non_abundant_numbers)


if __name__ == '__main__':
	print(non_abundant_sums())