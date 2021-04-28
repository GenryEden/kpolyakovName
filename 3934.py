def perebor(alphabet, previous, length):
	if length == 0:
		yield []
	else:
		for letter in alphabet:
			if letter < previous and letter % 2 != previous % 2:
				for word in perebor(alphabet, letter, length-1):
					if len(word) == length-1:
						yield [letter] + word

cnt = len(list(perebor(range(16), 17, 15)))
cnt += len(list(perebor(range(16), 18, 15)))

print(cnt)