# Powers of Two
# https://projecteuler.net/problem=686
import math

def power_of_two():
	# https://math.stackexchange.com/questions/4093970/powers-of-2-starting-with-123-does-a-pattern-exist
	# much easier to deal with logs of huge numbers
	# 2 ** j = 123abcd... = 10 ** x * 1.23abcd...
	# x + log(10)1.23 < log(10)2 ** j < x + log(10)1.24
	# log(10)1.23 < log(10)2 ** j - x < log(10)1.24
	# x = log(10)2 ** j
	lower = math.log(1.23, 10)
	upper = math.log(1.24, 10)
	j = 0
	count = 0
	while count != 678910:
		j += 1
		p = j * math.log(2, 10)
		if (lower < p - math.floor(p) < upper):
			count += 1

	return j


if __name__ == '__main__':
	print(power_of_two())