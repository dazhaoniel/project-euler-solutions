# Digit cancelling fractions
# https://projecteuler.net/problem=33
import math

def digit_canceling_fractions():
	numerator = 1
	denominator = 1
	for n in range(1, 10):
		for d in range(n, 10):
			for i in range(d, 10):
				if ((10 * n + i) * d == (10 * i + d) * n and n / d < 1):
					numerator *= n
					denominator *= d

	return denominator / math.gcd(numerator, denominator)


if __name__ == '__main__':
	print(digit_canceling_fractions())