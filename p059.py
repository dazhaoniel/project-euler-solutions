# XOR decryption
# https://projecteuler.net/problem=59
def decrypt(s, t):
	return ''.join(chr(a ^ ord(b)) for a, b in zip(s, t))

def xor_decryption():
	f = open('./p059_cipher.txt')
	text = f.read().strip().split(',')
	# convert string to int
	numbers = [int(x) for x in text]
	
	return numbers


if __name__ == '__main__':
	print(xor_decryption())