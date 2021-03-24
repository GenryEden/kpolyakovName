def perebor(alphabet, length):
	if length == 0:
		yield ''
		return 
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def check(x):
	if len(x) - 2 != len(set(x)):
		return False
	if x.count('А') != 2:
		return False
	if x.count('К') != 2:
		return False
	if 'АА' in x or 'КК' in x:
		return False
	return True

cnt = 0
last = ''
for word in set(perebor('КАПКАН', 6)):
	if check(word):
		last = word
		cnt += 1
print(cnt)