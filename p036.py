# Double-base palindromes
# https://projecteuler.net/problem=36
def is_palindrome(n):
	s = list(str(n))
	return s == s[::-1]

def double_based_palindromes():
	s = 0
	# print(bin(585))
	for i in range(1, 1000000):
		b = int(str(bin(i)).replace('0b', ''))
		if is_palindrome(i) and is_palindrome(b):
			s += i
	return s


if __name__ == '__main__':
	print(double_based_palindromes())