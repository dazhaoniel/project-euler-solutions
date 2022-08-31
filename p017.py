# Number letter counts
# https://projecteuler.net/problem=17
def number_to_letter(n):
	d = { 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
	12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
	17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
	30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
	80: 'eighty', 90: 'ninety', 100: 'hundred'}
	if (n <= 20):
		return len(d[n])
	elif (20 < n < 100):
		l = [int(char) for char in str(n)]
		return len(d[l[0]*10]) + len(d[l[1]])
	elif (100 <= n < 1000):
		l = [int(char) for char in str(n)]
		temp = len(d[l[0]]) + len(d[100])
		if (n % 100 == 0):
			return temp
		else:
			return temp + len('and') + number_to_letter(n % 100)
	elif n == 1000:
		return len('onethousand')
	else: return 0

def number_letter_counts():
	l = 0
	for x in range(1, 1001):
		l += number_to_letter(x)
	return l

if __name__ == '__main__':
	print(number_letter_counts())