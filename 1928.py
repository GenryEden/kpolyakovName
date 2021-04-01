def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	if word[0] == 'О':
		return False
	if 'АО' in word:
		return False
	return len(set(word)) == len(word)

cnt = 0 
for word in perebor('МАНОК', 5):
	if check(word):
		cnt += 1 
		# print(word)
		# input()

print(cnt)