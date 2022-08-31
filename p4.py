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


if __name__ == '__main__':
	print(largest_palindrome_product())