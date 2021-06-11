def perebor(alphabet, length):
	if length == 0:
		yield ''
	else:
		for letter in alphabet:
			for word in perebor(alphabet, length-1):
				yield letter+word

def calculator(n, program):
	for code in program:
		if code == '1':
			n += 1
		elif code == '2':
			n *= 2
			n -= 3
	return n

res = set()

for pr in perebor('12', 12):
	res.add(calculator(3, pr))

print(len(res))