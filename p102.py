# Triangle containment
# https://projecteuler.net/problem=102
def area(x1, y1, x2, y2, x3, y3):
	# area of triangle
	# https://stackoverflow.com/questions/55601927/correct-way-to-calculate-triangle-area-from-3-vertices 
	return abs(0.5*((x1-x3)*(y2-y1)-(x1-x2)*(y3-y1)))

def triangle_containment():
	# main idea is that ABP + APC + PBC
	f = open('./p102_triangles.txt')
	count = 0
	for line in f.readlines():
		x1, y1, x2, y2, x3, y3 = map(int, line.split(','))
		if area(x1, y1, x2, y2, x3, y3) == (area(x1, y1, x2, y2, 0, 0) + area(x1, y1, 0, 0, x3, y3) + area(0, 0, x2, y2, x3, y3)):
			count += 1

	return count

if __name__ == '__main__':
	print(triangle_containment())