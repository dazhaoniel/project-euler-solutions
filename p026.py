# Reciprocal cycles
# https://projecteuler.net/problem=26
def long_division_cycle(denom, num = 1):
	# long division
	# https://stackoverflow.com/questions/58167745/project-euler-problem-26-python-string-limits-in-fraction-numbers
	reminders = []
	rems = None
	while rems not in reminders:
		reminders.append(rems)
		num *= 10
		rems = num % denom
	reminders.pop(0)
	return len(reminders)

def reciprocal_cycles():
	count = 1
	val = 0
	for d in range(2, 1000):
		num = long_division_cycle(d)
		if num > count:
			count = num
			val = d

	return val


if __name__ == '__main__':
	print(reciprocal_cycles())