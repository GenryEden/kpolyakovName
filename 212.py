def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word[0] in 'ГД' and word[-1] in 'ГД'

cnt = 0
for word in perebor('ГОД', 6):
	cnt += check(word)

print(cnt)