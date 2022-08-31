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

if __name__ == '__main__':
	print(amicable_numbers())