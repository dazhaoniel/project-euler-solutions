# Champernowne's constant
# https://projecteuler.net/problem=40
def champernowne_constant():
	# 1st, 10th, 100th, 1000th, 10000th, 100000th and 1000000th
	# 9*1 + 90*2 + 900*3+ 9000*4 + 90000*5 + n*6 = 1000000
	# n ~= 185186
	s = ''
	for x in range(1, 185186):
		s += str(x)

	num = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

	return num

if __name__ == '__main__':
	print(champernowne_constant())
