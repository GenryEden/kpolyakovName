def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word[0] in 'МТР' and word[-1] in 'ЕО'

cnt = 0
for word in perebor('МЕТРО', 4):
	cnt += check(word)

print(cnt)