# Truncatable primes
# https://projecteuler.net/problem=37
from lib import prime3

def truncatable_primes():
	primes = prime3()
	c = s = 0

	while c != 11:
		for n in primes:
			if len(str(n)) > 1:
				flag = True
				for i in range(1, len(str(n))):
					num1 = int(str(n)[:i])
					num2 = int(str(n)[i:])
					if num1 not in primes or num2 not in primes:
						flag = False
						break
				if flag == True:
					print(n)
					c += 1
					s += n
	# n = 3797
	# for i in range(1, len(str(n))):
	# 	num1 = str(n)[:i]
	# 	num2 = str(n)[i:]
	# 	print(num1, num2)

	return c, s

if __name__ == '__main__':
	print(truncatable_primes())