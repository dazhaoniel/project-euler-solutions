# Square digit chains
# https://projecteuler.net/problem=92
# https://codereview.stackexchange.com/questions/31761/project-euler-problem-92-square-digit-chains
def get_digits(n):
	return list(map(int, str(n)))

def square_digit_chains():
	arrive = [None]*10000000
	arrive[1], arrive[89] = 1, 89
	for i in range(2, 10000000):
		chain = []
		while not arrive[i]:
			chain.append(i)
			i = sum(x**2 for x in get_digits(i))
		dest = arrive[i]
		for term in chain:
			arrive[term] = dest
	return arrive.count(89)



if __name__ == '__main__':
	print(square_digit_chains())
