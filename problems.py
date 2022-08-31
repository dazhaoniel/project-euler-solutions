# Multiples of 3 or 5
# https://projecteuler.net/problem=1
def find_multiples():
	s = 0
	for x in range(1000):
		if x%3 == 0 or x%5 == 0:
			s += x

	return s


# Even Fibonacci numbers
# https://projecteuler.net/problem=2
def even_fib_numbers():
	s = 2
	x = 1
	y = 2
	while y <= 4000000:
		n = x + y
		x = y
		y = n
		if n%2 == 0:
			s += n

	return s


# Largest prime factor
# https://projecteuler.net/problem=3
import math

def largest_prime_factor(n):
	while n % 2 == 0:
		n = n / 2

	for i in range(3, int(math.sqrt(n)), 2):
		# while i divides n, print i and divide n
		while n % i == 0:
			n = n / i
			print(i)


# Largest palindrome product
# https://projecteuler.net/problem=4
def is_palindrome(s):
	#reverse a list
	return s == s[::-1]


def largest_palindrome_product():
	greatest = 0
	for x in reversed(range(100, 1000)):
		for y in reversed(range(100, 1000)):
			num = x*y

			l = [c for c in str(num)]
			if is_palindrome(l):
				if num > greatest:
					greatest = num

	return greatest


# Smallest multiple
# https://projecteuler.net/problem=5
from functools import reduce

def lcm(a, b):
	return a * b // math.gcd(a, b)

def smallest_multiple():
	return reduce(lcm, range(1, 20+1))


# Sum square difference
# https://projecteuler.net/problem=6
def sum_square_difference():
	sum_of_square = sum(i ** 2 for i in range(1, 101))
	square_of_sum = sum(range(1, 101)) ** 2

	return square_of_sum - sum_of_square


# 10001st prime
# https://projecteuler.net/problem=7
def is_prime(n):
	for i in range(2, n // 2 + 1):
		if (n % i == 0):
			return False
	return True

def find_prime():
	count = 1
	n = 3
	while n > 0:
		if is_prime(n):
			count += 1
		if (count == 10001):
		 	return n
		n += 1
	# while count <= 10001:
	# 	if is_prime(n):
	# 		count += 1
	# 	n += 1

	# return n


# Largest product in a series
# https://projecteuler.net/problem=8
import numpy

def largest_product():
	series = """
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    """

	series = series.replace(' ', '').replace('\n', '')
	series_list = [int(char) for char in series]
	# print(series_list)
	largest = 0

	# 13 adjacent digits
	for i in range(len(series_list)-12):
		prod = numpy.prod(series_list[i:i+13])
		if (prod > largest):
			largest = prod

	return largest


# Special Pythagorean triplet
# https://projecteuler.net/problem=9
# a + b + c = 1000
# a^2 + b^2 = c^2
def special_pythagorean_triplet():
	a = b = c = 0
	s = 1000
	for a in range(1, s // 3):
		for b in range(a, s // 2):
			c = s - a - b
			if (a * a + b * b == c * c):
				print(a, b, c)
				return a * b * c


# Summation of primes
# https://projecteuler.net/problem=10
def summation_of_primes():
	# use list comprehension
	primes = [x for x in range(2, 2000001) if is_prime(x)]
	s = sum(primes)
	return s


# Largest product in a grid
# https://projecteuler.net/problem=11
arr =[[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8,],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0,],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65,],
[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91,],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,],
[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50,],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,],
[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21,],
[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,],
[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95,],
[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92,],
[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57,],
[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58,],
[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40,],
[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66,],
[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69,],
[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36,],
[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16,],
[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54,],
[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

def largest_product():
	greatest = 1
	l = len(arr)
	for column in range(l):
		for row in range(l):
			# horizontally
			product = 1
			for i in range(4):
				if (row + i < l):
					product *= arr[row + i][column]
					if product > greatest:
						greatest = product

			# vertically
			product = 1
			for i in range(4):
				if (column + i < l):
					product *= arr[row][column + i]
					if product > greatest:
						greatest = product

			# diagnally upward
			product = 1
			for i in range(4):
				if (column + i < l) and (row + i < l):
					product *= arr[row - i][column + i]
					if product > greatest:
						greatest = product

			# diagnally downward
			product = 1
			for i in range(4):
				if (column + i < l) and (row + i < l):
					product *= arr[row + i][column + i]
					if product > greatest:
						greatest = product

	return greatest
			

# Highly divisible triangular number
# https://projecteuler.net/problem=12
def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n) + 1)) if not n % i)

def triangle(n):
    return ((n ** 2) + n) // 2

def find_triangle_number():
	i = 1
	c = 1
	while (c <= 500):
		n = triangle(i)
		c = get_factors(n)
		i += 1
	return n


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




