def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word


def check(word):
	if not(word.count('А') == 1 == word.count('Й')):
		return False
	return word[0] != 'Й'

cnt = 0

for word in perebor('АНДРЕЙ', 7):
	cnt += check(word)

print(cnt)