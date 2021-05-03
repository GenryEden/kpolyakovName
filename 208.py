def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word.count('X') == 0 or (word[-1] == 'X' and word.count('X') == 1)

cnt = 0
for word in perebor('ABCX', 5):
	cnt += check(word)

print(cnt)