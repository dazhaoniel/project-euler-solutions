# Digit fifth powers
# https://projecteuler.net/problem=30
# upper bound n ≤ 6 * 9 ** 5
def digit_fifth_powers():
	answer = 0
	for n in range(2, (9 ** 5) * 6):
		t = [int(char) ** 5 for char in str(n)]
		if (sum(t) == n): answer += n

	return answer


if __name__ == '__main__':
	print(digit_fifth_powers())