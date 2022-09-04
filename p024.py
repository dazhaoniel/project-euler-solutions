# Lexicographic permutations
# https://projecteuler.net/problem=24
# https://www.mbatious.com/topic/336/how-to-find-out-rank-of-a-word-in-a-dictionary
from itertools import permutations

def lexicographic_permutations():
	p = permutations('0123456789')
	return ''.join(list(p)[999999])


if __name__ == '__main__':
	print(lexicographic_permutations())