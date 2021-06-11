def calculator(n, prg):
	for cmd in prg:
		if cmd == '1':
			n += 3
		else:
			n *= 2
			n += 1
	return n

def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

ans = set()

for word in perebor('12', 13):
	ans.add(calculator(2, word))

print(len(ans))