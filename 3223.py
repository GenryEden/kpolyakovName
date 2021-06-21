def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	if word.count('Й') > 1:
		return False
	if word[0] == 'Й':
		return False
	if word[-1] == 'Й':
		return False
	if 'ЙЕ' in word or 'ЕЙ' in word:
		return False
	return True



ans = set()
for word in perebor(''.join(set('СОЛОВЕЙ')), 6):
	if check(word):
		ans.add(word)

print(len(ans))