# Pentagon numbers
# https://projecteuler.net/problem=44
def is_pentagon(n):
	return (1+(24*n+1)**0.5) % 6 == 0
	
def pentagon_numbers():
	i = 1
	while True:
		for j in range(1, i):
			a = i*(3*i-1)/2
			b = j*(3*j-1)/2
			if is_pentagon(a+b) and is_pentagon(a-b):
				return a-b
		i += 1


if __name__ == '__main__':
	print(pentagon_numbers())
