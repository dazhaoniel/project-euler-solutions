# Names scores
# https://projecteuler.net/problem=22
from string import ascii_uppercase

def score(name):
	return sum(ascii_uppercase.index(char) + 1 for char in name)

def name_scores():
	lines = open('./p022_names.txt').read().replace('\"', '').split(',')
	lines.sort()

	return sum(score(n) * (i + 1) for i, n in enumerate(lines))

if __name__ == '__main__':
	print(name_scores())