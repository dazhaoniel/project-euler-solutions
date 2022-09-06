# How many reversible numbers are there below one-billion?
# https://projecteuler.net/problem=145
def reverse(n):
	return int(str(n)[::-1])

def all_odd_digits(n):
    return all(int(i)%2 != 0 for i in str(n))

def count_reversibles():
	l = set([])
	for i in range(10**9):
		if (i%10 != 0):
			s = reverse(i) + i
			if all_odd_digits(s):
				l.add(reverse(i))
				l.add(i)
			

	return len(l)


if __name__ == '__main__':
	print(count_reversibles())