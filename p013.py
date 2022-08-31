# Large sum
# https://projecteuler.net/problem=13
def large_sum():
	file = open('p013.txt', 'r')
	l = [int(line.replace('\n', '')) for line in file.readlines()]
	s = sum(l)
	return s

if __name__ == '__main__':
	print(large_sum())