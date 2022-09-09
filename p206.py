# Concealed Square
# https://projecteuler.net/problem=206
def match(n):
	template = '1_2_3_4_5_6_7_8_9_0'
	s = str(n)
	return all(s[i] == template[i] for i in range(0, len(s), 2))

def concealed_square():
	# 1_2_3_4_5_6_7_8_9 x 10
	# only squares of 3, 7 end with 9
	# start with n = 138902663, the square root of max number 19293949596979899
	n = 138902663
	while not match(n*n): n -= 2
	return n*10
	


if __name__ == '__main__':
	print(concealed_square())