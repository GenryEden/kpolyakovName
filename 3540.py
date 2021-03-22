def perebor(alphabet, length):
	if length == 0:
		yield ''
		return
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter + word

def check(word):
	if word[0] == 'Ь':
		return False

	if len(word) != len(set(word)):
		return False

	ind = word.index('Ь')
	if word[ind-1] in vowels:
		return False

	return True

alphabet = 'ЗАПИСЬ'
vowels = 'АИ'
cnt = 0
for word in perebor(alphabet, 6):
	if check(word):
		cnt += 1
print(cnt)