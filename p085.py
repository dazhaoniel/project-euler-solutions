# Counting rectangles
# https://projecteuler.net/problem=85
def counting_rectangles():
	# https://en.wikipedia.org/wiki/Triangular_number
	# based on number of triangles, number of rectangles would be
	# (x**2+x)*(y**2+y)/4
	area = 0
	closest = 2000000
	for x in range(1, 100):
		for y in range(1, 100):
			n = (x**2+x)*(y**2+y)/4
			if (n < 2000000 and abs(n-2000000) < closest):
				closest = abs(n-2000000)
				area = x*y
	return area

if __name__ == '__main__':
	print(counting_rectangles())