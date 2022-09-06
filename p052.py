# Permuted multiples
# https://projecteuler.net/problem=52
def permuted_multiples():
	x = 1
	while True:
		if set(str(x)) == set(str(x*2)) and set(str(x)) == set(str(x*3)) and set(str(x)) == set(str(x*4)) and set(str(x)) == set(str(x*5)) and set(str(x)) == set(str(x*6)):
			return x
		x += 1

if __name__ == '__main__':
	print(permuted_multiples())