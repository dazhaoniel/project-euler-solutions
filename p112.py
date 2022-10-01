# Bouncy numbers
# https://projecteuler.net/problem=112
def is_bouncy(n):
	if sorted(list(str(n))) == list(str(n)) or sorted(list(str(n))) == list(str(n))[::-1]:
		return False
	return True

def bouncy_numbers():
	bouncy = 0
	total = 0
	n = 1
	while n>0:
		if is_bouncy(n): 
			bouncy += 1
		total += 1
		if bouncy/total == 0.99:
			return n
		n += 1


if __name__ == '__main__':
	print(bouncy_numbers())
