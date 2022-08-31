# Large sum
# https://projecteuler.net/problem=13
def large_sum():
	file = open('p13.txt', 'r')
	l = [int(line.replace('\n', '')) for line in file.readlines()]
	s = sum(l)
	return s


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

# Lattice paths
# https://projecteuler.net/problem=15
def nck(n, k):
	# https://en.wikipedia.org/wiki/Binomial_coefficient
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def lattice_paths():
	return nck(20 + 20, 20)
	

# Power digit sum
# https://projecteuler.net/problem=16
def power_digit_sum():
	num = 2 ** 1000
	return sum([int(char) for char in str(num)])


# Number letter counts
# https://projecteuler.net/problem=17
def number_to_letter(n):
	d = { 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
	12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
	17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
	30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
	80: 'eighty', 90: 'ninety', 100: 'hundred'}
	if (n <= 20):
		return len(d[n])
	elif (20 < n < 100):
		l = [int(char) for char in str(n)]
		return len(d[l[0]*10]) + len(d[l[1]])
	elif (100 <= n < 1000):
		l = [int(char) for char in str(n)]
		temp = len(d[l[0]]) + len(d[100])
		if (n % 100 == 0):
			return temp
		else:
			return temp + len('and') + number_to_letter(n % 100)
	elif n == 1000:
		return len('onethousand')
	else: return 0

def number_letter_counts():
	l = 0
	for x in range(1, 1001):
		l += number_to_letter(x)
	return l


# Maximum path sum I
# https://projecteuler.net/problem=18
def maximum_path_sum():
	number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

	number = number.strip().split('\n')
	numbers_list = [i.split(' ') for i in number]

	# bottom up approach
	for i in range(len(numbers_list)-2,-1,-1):
		for j in range(len(numbers_list[i])):
			numbers_list[i][j] = int(numbers_list[i][j]) + max(int(numbers_list[i+1][j]), int(numbers_list[i+1][j+1]))
		
	return numbers_list[0][0]


# Counting Sundays
# https://projecteuler.net/problem=19
from datetime import date, timedelta

def counting_sundays():
	start = date(1901, 1, 1)
	end = date(2001, 1, 1)
	delta = timedelta(days=1)
	count = 0
	while start < end:
		if (start.weekday() == 6 and start.day == 1):
			count += 1
		start += delta

	return count


# Factorial digit sum
# https://projecteuler.net/problem=20
def factorial_digit_sum():
	n = 1
	for i in range(100, 0, -1):
		n *= i
	
	s = 0

	for char in str(n):
		s += int(char)

	return s



if __name__ == '__main__':
	print(factorial_digit_sum())




