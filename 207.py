def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word.count('С') == 1

ans = 0
for word in perebor('СЛОН', 5):
	if check(word):
		ans += 1

print(ans)