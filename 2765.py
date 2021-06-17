def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def calculator(prg, n):
	for cmd in prg:
		if cmd == '1':
			n += 1
		elif cmd == '2':
			n += 4
		else:
			n *= 2
	return n

cnt = 0
for prg in perebor('123', 7):
	if calculator(prg, 3) == 27:
		cnt += 1

print(cnt)