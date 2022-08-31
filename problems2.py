# Amicable numbers
# https://projecteuler.net/problem=21
def d(n):
	num = set()
	for i in range(1, n):
		if (n % i == 0):
			num.add(i)

	return sum(num)

def amicable_numbers():
	num = set()
	for i in range(1, 10001):
		n = d(i)
		if (i == d(n) and i != n):
			num.add(i)
			num.add(n)

	return sum(num)


# Names scores
# https://projecteuler.net/problem=22
from string import ascii_uppercase
def score(name):
	return sum(ascii_uppercase.index(char) + 1 for char in name)

def name_scores():
	lines = open('./p022_names.txt').read().replace('\"', '').split(',')
	lines.sort()

	return sum(score(n) * (i + 1) for i, n in enumerate(lines))
	

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


# Lexicographic permutations
# https://projecteuler.net/problem=24
# TODO

# 1000-digit Fibonacci number
# https://projecteuler.net/problem=25
def thousand_digit_fib_number():
	count = 3
	x = 1
	y = 2
	while y > 0:
		n = x + y
		x = y
		y = n
		count += 1
		if (len(str(n)) == 1000):
			break
	return count


# Reciprocal cycles
# https://projecteuler.net/problem=26
def long_division_cycle(denom, num = 1):
	# long division
	# https://stackoverflow.com/questions/58167745/project-euler-problem-26-python-string-limits-in-fraction-numbers
	reminders = []
	rems = None
	while rems not in reminders:
		reminders.append(rems)
		num *= 10
		rems = num % denom
	reminders.pop(0)
	return len(reminders)

def reciprocal_cycles():
	count = 1
	val = 0
	for d in range(2, 1000):
		num = long_division_cycle(d)
		if num > count:
			count = num
			val = d

	return val


# Quadratic primes
# https://projecteuler.net/problem=27
from problems import is_prime

primes = [
   2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997];    

def consecutive_primes(a, b):
	n = 1
	while is_prime(abs(n ** 2 + a * n + b)):
		n += 1
	return n

def quadratic_primes():
	max_count = 0
	for a in range(-999, 1000, 2):
		for b in primes:
			n = consecutive_primes(a, b)
			if (n > max_count):
				max_count = n
				answer = a, b

	a, b = answer
	print(a, b)
	return a * b


# Number spiral diagonals
# https://projecteuler.net/problem=28
def number_spiral_diagonals():
	sum = 1
	n = 1
	while ((n + 2) ** 2 <= 1001 * 1001):
		sum += (n + 2) ** 2 * 4 - (n + 1) * 6
		n += 2
	return sum


# Distinct powers
# https://projecteuler.net/problem=29
def distinct_powers():
	numbers_list = set()
	for a in range(2, 101):
		for b in range (2, 101):
			numbers_list.add(a ** b)

	return len(numbers_list)


# Digit fifth powers
# https://projecteuler.net/problem=30
# upper bound n ≤ 6 * 9 ** 5
def digit_fifth_powers():
	answer = 0
	for n in range(2, (9 ** 5) * 6):
		t = [int(char) ** 5 for char in str(n)]
		if (sum(t) == n): answer += n

	return answer


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


# Pandigital products
# https://projecteuler.net/problem=32
def pandigital_products():
	num = set('123456789')
	answer = set()
	# x is 1 digit and y is 4 digits
	for x in range(1, 10):
		for y in range(1000, 10000):
			s = str(x) + str(y) + str(x * y)
			if len(s) != 9: break
			if (set(s) == num): answer.add(x * y)

	# x is 2 digits and y is 3 digits
	for x in range(10, 100):
		for y in range(100, 1000):
			s = str(x) + str(y) + str(x * y)
			if len(s) != 9: break
			if (set(s) == num): answer.add(x * y)

	return sum(answer)


# Digit cancelling fractions
# https://projecteuler.net/problem=33



if __name__ == '__main__':
	print(pandigital_products())
	



