# Distinct powers
# https://projecteuler.net/problem=29
def distinct_powers():
	numbers_list = set()
	for a in range(2, 101):
		for b in range (2, 101):
			numbers_list.add(a ** b)

	return len(numbers_list)

if __name__ == '__main__':
	print(distinct_powers())