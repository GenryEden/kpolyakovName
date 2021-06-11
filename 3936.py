def perebor(length, previous):
	if length == 0:
		yield ''
	else:
		for i in range(0, 10):
			if i < previous and i % 2 != previous % 2:
				for word in perebor(length-1, i):
					yield str(i)+word

print(len(list(perebor(6, 10))) + len(list(perebor(6, 11))))