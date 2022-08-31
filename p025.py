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


if __name__ == '__main__':
	print(thousand_digit_fib_number())