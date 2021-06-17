def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	if word[0] == 'Й':
		return False
	return 'Е' in word or 'И' in word


ans = set()

for word in perebor('ЕНИСЕЙ', 4):
	if check(word):
		ans.add(word)

print(len(ans))
