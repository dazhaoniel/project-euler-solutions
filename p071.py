# Ordered fractions
# https://projecteuler.net/problem=71
def ordered_fractions():
	# https://en.wikipedia.org/wiki/Farey_sequence
	# n/d < 3/7
	# d*a-b*n = 1
	d = 1000000
	while (d*3%7 != 1):
		d -= 1
	return ((d*3)-1)/7

if __name__ == '__main__':
	print(ordered_fractions())