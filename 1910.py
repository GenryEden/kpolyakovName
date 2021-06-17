def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(word):
	toCount = 'РСТМ'
	cnt = 0
	for s in word:
		if s in toCount:
			cnt += 1
	return cnt >= 3


ans = set()

for word in perebor('РУСТАМ', 6):
	if check(word):
		ans.add(word)

print(len(ans))