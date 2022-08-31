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


if __name__ == '__main__':
	print(counting_sundays())