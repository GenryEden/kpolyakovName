def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word.count('X') == 1

cnt = 0
for word in perebor('ABCDX', 4):
	if check(word):
		cnt += 1

print(cnt)