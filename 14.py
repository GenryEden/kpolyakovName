def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield word+letter

def check(word):
	return word.count('П') == 1

cnt = 0

for word in perebor('ПИР', 5):
	if check(word):
		cnt += 1

print(cnt)