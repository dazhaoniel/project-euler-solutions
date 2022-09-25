# Cubic permutations
# https://projecteuler.net/problem=62

def cubic_permutations():
	# generate cubes until we find 5 that gives the same permutation
	i = 1
	cubes = []
	while True:
		cube = sorted(list(str(i**3)))
		cubes.append(cube)
		if (cubes.count(cube) == 5):
			return (cubes.index(cube)+1)**3
		i += 1


if __name__ == '__main__':
	print(cubic_permutations())