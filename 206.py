def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word.count('A') == 2


cnt = 0
for word in perebor('ACGT', 5):
	if check(word):
		cnt += 1

print(cnt)