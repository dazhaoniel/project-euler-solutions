# Integer right triangles
# https://projecteuler.net/problem=39
import math
from collections import Counter

def integer_right_triangles():
	cnt = Counter()
	for a in range(1, 1000):
		for b in range(a, 1000):
			c = math.sqrt(a ** 2 + b ** 2)
			s = a + b + c
			if (int(c) == c and s <= 1000):
				cnt[s] += 1

	return cnt.most_common(1)

if __name__ == '__main__':
	print(integer_right_triangles())