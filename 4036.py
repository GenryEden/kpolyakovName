def calculator(n, prg):
	for i in prg:
		if i == '1':
			n *= 2
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

for prg in perebor('12', 15):
	ans.add(calculator(1, prg))

print(len(ans))