def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	return word.count('К') == 2

ans = 0
for word in perebor('КАНТ', 6):
	ans += check(word)

print(ans)