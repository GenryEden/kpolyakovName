def perebor(alphabet, length):
	if length == 0:
		yield ''
		return
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	if len(word) != len(set(word)):
		return False
	if word[0] == 'Й':
		return False
	if 'ОЙ' in word:
		return False

	return True
cnt = 0
for word  in perebor('КРОЙ', 4):
	if check(word):
		print(word)
		cnt += 1
print(cnt)